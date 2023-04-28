from django.utils import timezone
import random
from datetime import datetime
from datetime import time
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from django.db import IntegrityError
from django.core.cache import cache


from .models import User, Weather, Animal, CapturedAnimal, Trade, Background, SpecialAnimal, CapturedSpecialAnimal
from .serializers import WeatherSerializer, AnimalSerializer, CapturedAnimalSerializer, TradeSerializer, BackgroundSerializer, SpecialAnimalSerializer, CapturedSpecialAnimalSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response()


class AnimalListView(generics.ListAPIView):
    '''List all animals
    '''
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class BackgroundView(generics.ListAPIView):
    ''' fetch background for the right time of day
    '''
    serializer_class = BackgroundSerializer

    def get_queryset(self):
        queryset = Background.objects.all()
        code = self.request.query_params.get('code')[0]

        now = datetime.now().time()

        if time(7) <= now <= time(20):
            queryset = queryset.filter(code=code, day_or_night='am')
        else:
            queryset = queryset.filter(code=code, day_or_night='pm')
        return queryset


class CapturedAnimalView(APIView):
    '''logged in user captures animal or removes an animal
    '''

    def post(self, request, name, variation):
        owner = request.user
        animal = get_object_or_404(
            Animal, name__iexact=name, variation_type__iexact=variation)

        captured_animal, created = CapturedAnimal.objects.get_or_create(
            owner=owner, animal=animal,
            defaults={'last_capture_date': datetime.now(timezone.utc), 'points': 0})

        if not created:
            last_capture_date = captured_animal.last_capture_date
            time_difference = (datetime.now(timezone.utc) -
                               last_capture_date).total_seconds()

            #  86400 seconds for 24 hours
            # 43200 seconds for 12 hours
            if time_difference < 43200:
                return Response(
                    {"error": "You have already captured this animal within 12 hours!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                captured_animal.last_capture_date = datetime.now(timezone.utc)
                captured_animal.points += 1
                captured_animal.save()

        # SpecialAnimal created when 10 point reached
        if captured_animal.points == 10:
            special_animal = SpecialAnimal.objects.filter(
                animal__name__iexact=name, animal__variation_type__iexact=variation).first()
            if special_animal:
                special_captured, created = CapturedSpecialAnimal.objects.get_or_create(
                    owner=owner, special_animal=special_animal)
                serializer = CapturedSpecialAnimalSerializer(
                    special_captured, context={'request': request})
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer = CapturedAnimalSerializer(
            captured_animal, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, name, variation):
        owner = request.user
        animal = get_object_or_404(
            Animal, name__iexact=name, variation_type__iexact=variation)

        release_animal = get_object_or_404(
            CapturedAnimal, owner=owner, animal=animal)
        release_animal.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAnimalListView(generics.ListAPIView):
    ''' list of all the user's caught animals
    '''

    serializer_class = CapturedAnimalSerializer

    def get_queryset(self):
        owner = self.request.user
        return CapturedAnimal.objects.filter(owner=owner)


class UserSpecialAnimalListView(generics.ListAPIView):
    ''' list of all the user's special animals
    '''

    serializer_class = CapturedSpecialAnimalSerializer

    def get_queryset(self):
        owner = self.request.user
        return CapturedSpecialAnimal.objects.filter(owner=owner)


class AnimalDetailView(APIView):
    ''' display information about animal passed in
    '''

    def get(self, request, name, variation_type):
        animal = Animal.objects.get(
            name__iexact=name, variation_type__iexact=variation_type)
        serializer = AnimalSerializer(animal)

        return Response(serializer.data)


class TradeView(APIView):
    ''' allow users to make a trade animals request
    '''

    def post(self, request):
        trade_starter = request.user

        offered_animal_data = request.data.get("offered_animal")
        desired_animal_data = request.data.get("desired_animal")
        trade_receiver_username = request.data.get("trade_receiver")

        trade_receiver = get_object_or_404(
            User, username=trade_receiver_username)

        offered_animal = get_object_or_404(
            CapturedAnimal, animal__name=offered_animal_data, owner=trade_starter)

        desired_animal = get_object_or_404(
            CapturedAnimal, animal__name=desired_animal_data, owner=trade_receiver)

        trade = Trade.objects.create(
            trade_starter=trade_starter,
            trade_receiver=trade_receiver,
            offered_animal=offered_animal,
            desired_animal=desired_animal,
        )

        serializer = TradeSerializer(trade)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MyTradeOfferView(generics.ListAPIView):
    ''' List all offers logged in user started
    '''

    serializer_class = TradeSerializer

    def get_queryset(self):
        trade_starter = self.request.user
        return Trade.objects.filter(trade_starter=trade_starter)


class MyReceivedOfferView(generics.ListAPIView):
    ''' List all received offers made to user from other people
    '''

    serializer_class = TradeSerializer

    def get_queryset(self):
        trade_receiver = self.request.user
        return Trade.objects.filter(trade_receiver=trade_receiver)


class TradeAcceptView(APIView):
    ''' allow trade receiver to accept a trade request and swap animals
    '''

    def post(self, request, trade_id):
        trade = get_object_or_404(Trade, id=trade_id, status='pending')
        trade_receiver = request.user

        if trade.trade_receiver != trade_receiver:
            return Response({'detail': 'You are not authorized to accept this trade request.'}, status=status.HTTP_401_UNAUTHORIZED)

        # swap animals
        offered_animal = trade.offered_animal
        desired_animal = trade.desired_animal
        offered_animal.owner, desired_animal.owner = desired_animal.owner, offered_animal.owner
        offered_animal.save()
        desired_animal.save()

        # update the trade status
        trade.status = 'accepted'
        trade.save()

        serializer = TradeSerializer(trade)

        return Response(serializer.data)


class WeatherAnimalView(generics.RetrieveAPIView):
    '''fetch random animal of weather type given in url
    '''

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_object(self, *args, **kwargs):
        original_code = self.kwargs["original_code"]
        if original_code == 800:
            weather_code = 9
        else:
            weather_code = (str(original_code))[0]

        animals = Animal.objects.filter(weather__weather_code=weather_code)
        animals = list(animals)

        random_animal = random.choice(animals)

        return random_animal
