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
    weather = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'image',
            'weather'
        )

    def get_weather(self, obj):
        WEATHER_MAP = {
            2: 'Thunderstorm',
            3: 'Drizzle',
            5: 'Rain',
            6: 'Snow',
            7: 'Atmosphere',
            8: 'Clear',
        }

        return WEATHER_MAP.get(obj.weather.weather_code, '')


class CapturedAnimalSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    animal = serializers.StringRelatedField(many=False)

    class Meta:
        model = CapturedAnimal
        fields = (
            'owner',
            'animal'
        )
