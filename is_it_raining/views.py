import random
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from django.utils.text import slugify

from .models import User, Weather, Animal, CapturedAnimal, Trade, AnimalImage, WeatherIcon
from .serializers import WeatherSerializer, AnimalSerializer, CapturedAnimalSerializer, TradeSerializer, WeatherIconSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response()


class AnimalListView(generics.ListAPIView):
    '''List all animals
    '''
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


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


class WeatherIconView(generics.RetrieveAPIView):
    ''' retreieve weather icon
    '''
    queryset = WeatherIcon.objects.all()
    serializer_class = WeatherIconSerializer
    lookup_field = 'icon_code'


class CapturedAnimalView(APIView):
    '''logged in user captures animal or removes an animal
    '''

    def post(self, request, name):
        owner = request.user
        animal = get_object_or_404(Animal, name__iexact=name)

        captured = CapturedAnimal.objects.create(owner=owner, animal=animal)
        serializer = CapturedAnimalSerializer(captured)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, name):
        owner = request.user
        animal = get_object_or_404(Animal, name__iexact=name)

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


class AnimalDetailView(generics.RetrieveAPIView):
    '''display information about animal passed in
    '''
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'name__iexact'


class TradeView(APIView):
    ''' allow users to trade animals
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
