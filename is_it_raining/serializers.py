from rest_framework import serializers
from .models import Weather, Animal, CapturedAnimal


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = (
            'id',
            'weather_code'
        )


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'weather',
            'image'
        )


class CapturedAnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = CapturedAnimal
        fields = (
            'owner',
            'animal'
        )
