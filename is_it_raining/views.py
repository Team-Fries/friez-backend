from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework.views import APIView

from .models import User, Weather, Animal


@api_view(["GET"])
def api_root(request, format=None):
    return Response()


class WeatherAnimalView(APIView):
    def get(request, *args, **kwargs):
        # get code from url for kwarg
        weather_code = self.kwargs["weather_code"]
        # search weather using code, create if none
        weather, created = Weather.objects.get_or_create(
            weather_code=weather_code)
