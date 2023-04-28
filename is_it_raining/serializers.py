import random
from datetime import datetime
from django.utils import timezone
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from .models import Weather, Animal, CapturedAnimal, Trade, Background


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = (
            'id',
            'weather_code'
        )


class BackgroundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Background
        fields = (
            'id',
            'name',
            'background_image',
            'day_or_night',
            'code'
        )


class AnimalSerializer(serializers.ModelSerializer):
    weather = serializers.SerializerMethodField()
    can_capture = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'weather',
            'variation_type',
            'image',
            'can_capture',
        )

    def get_weather(self, obj):
        WEATHER_MAP = {
            2: 'Thunderstorm',
            3: 'Drizzle',
            5: 'Rain',
            6: 'Snow',
            7: 'Atmosphere',
            8: 'Clouds',
            9: 'Clear'
        }

        return WEATHER_MAP.get(obj.weather.weather_code, '')

    def get_can_capture(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False

        # Check if the user has captured this animal before
        try:
            captured_animal = CapturedAnimal.objects.get(
                owner=request.user, animal=obj)
        except CapturedAnimal.DoesNotExist:
            return True

        # Calculate the time difference between now and the last capture date
        last_capture_date = captured_animal.last_capture_date
        time_difference = (datetime.now(timezone.utc) -
                           last_capture_date).total_seconds()

        # Check if enough time has passed for the user to capture the animal again
        if time_difference < 43200:
            return False
        else:
            return True


class CapturedAnimalSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    animal = AnimalSerializer()
    points = serializers.IntegerField()

    class Meta:
        model = CapturedAnimal
        fields = (
            'owner',
            'animal',
            'points',
        )

    validators = [
        UniqueTogetherValidator(
            queryset=CapturedAnimal.objects.all(),
            fields=('owner', 'animal__variation_type'),
        )
    ]


class TradeSerializer(serializers.ModelSerializer):
    trade_starter = serializers.StringRelatedField(many=False)
    trade_receiver = serializers.StringRelatedField(many=False)
    offered_animal = serializers.SerializerMethodField()
    desired_animal = serializers.SerializerMethodField()

    class Meta:
        model = Trade
        fields = (
            'id',
            'trade_starter',
            'trade_receiver',
            'status',
            'offered_animal',
            'desired_animal',
        )

    def get_offered_animal(self, obj):
        return obj.offered_animal.animal.name

    def get_desired_animal(self, obj):
        return obj.desired_animal.animal.name
