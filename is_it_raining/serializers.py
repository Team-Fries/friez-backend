from rest_framework import serializers
from .models import Weather, Animal, CapturedAnimal, AnimalImage


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


class AnimalImageSerializer(serializers.ModelSerializer):
    model = AnimalImage
    fields = (
        'id',
        'animal',
        'name'
    )


class CapturedAnimalSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    animal = serializers.StringRelatedField(many=False)

    class Meta:
        model = CapturedAnimal
        fields = (
            'owner',
            'animal'
        )
