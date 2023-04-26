import random
from rest_framework import serializers
from .models import Weather, Animal, CapturedAnimal, Trade, WeatherIcon, Background


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


class WeatherIconSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherIcon
        fields = (
            'id',
            'icon_code',
            'icon_image',
            'is_day'
        )


class AnimalSerializer(serializers.ModelSerializer):
    # random_image = serializers.SerializerMethodField()
    weather = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'weather',
            'variation_type',
            'image',
            # 'random_image'
        )

    # def get_random_image(self, obj):
    #     images = obj.images.order_by("?")
    #     if images:
    #         image = images.first()
    #         return image.image.url
    #     return None

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


class CapturedAnimalSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    animal = AnimalSerializer()

    class Meta:
        model = CapturedAnimal
        fields = (
            'owner',
            'animal'
        )


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
