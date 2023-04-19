import random
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework.views import APIView

from .models import User, Weather, Animal
from .serializers import WeatherSerializer, AnimalSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response()


class AnimalListView(generics.ListAPIView):
    '''List all animals
    '''
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetailView(generics.RetrieveAPIView):
    '''fetch random animal of weather type given in url
    '''
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    def get_object(self, *args, **kwargs):
        original_code = self.kwargs["original_code"]
        weather_code = (str(original_code))[0]
        animals = Animal.objects.filter(weather__weather_code=weather_code)
        animals = list(animals)
        random_animal = random.choice(animals)
        return random_animal
