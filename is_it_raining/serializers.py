import random
from datetime import datetime
from django.utils import timezone
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers
from .models import Weather, Animal, CapturedAnimal, Trade, Background, SpecialAnimal, CapturedSpecialAnimal


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
            'code',
            'audio_file',
        )


class SpecialAnimalSerializer(serializers.ModelSerializer):
    special_name = serializers.CharField(source='animal.name')
    special_type = serializers.CharField(source='animal.variation_type')
    image = serializers.StringRelatedField(many=False)

    class Meta:
        model = SpecialAnimal
        fields = (
            'special_name',
            'special_type',
            'image',
        )


class AnimalSerializer(serializers.ModelSerializer):
    weather = serializers.SerializerMethodField()
    can_capture = serializers.SerializerMethodField()
    points_left_until_max = serializers.SerializerMethodField()
    catch_um_song = serializers.SerializerMethodField()
    special_animal = SpecialAnimalSerializer(many=True)

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'weather',
            'variation_type',
            'image',
            'can_capture',
            'points_left_until_max',
            'catch_um_song',
            'special_animal',
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
        # get the current request object, which is passed to the serializer context.
        request = self.context.get('request')

        # checks if the request object is None or if the user is not authenticated.
        # If either of these conditions is true, then the user cannot capture the animal, so it returns False.
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
        if time_difference < 60:
            return False
        else:
            return True

    def get_points_left_until_max(self, obj):
        request = self.context.get('request')

        if not request or not request.user.is_authenticated:
            return None
        try:
            captured_animal = CapturedAnimal.objects.get(
                owner=request.user, animal=obj)
        except CapturedAnimal.DoesNotExist:
            return None

        points_left = max(10 - captured_animal.points, 0)
        if points_left <= 0:
            return 0
        else:
            return points_left

    def get_catch_um_song(self, obj):
        if self.get_can_capture(obj):
            return 'https://team-fries-images.s3.us-east-2.amazonaws.com/music/catchum-correct.wav'
        else:
            return ''


class CapturedAnimalSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    animal = AnimalSerializer()
    points = serializers.IntegerField()
    animal_lobby_song = serializers.SerializerMethodField()

    class Meta:
        model = CapturedAnimal
        fields = (
            'owner',
            'animal',
            'points',
            'animal_lobby_song',
        )

    validators = [
        UniqueTogetherValidator(
            queryset=CapturedAnimal.objects.all(),
            fields=('owner', 'animal__variation_type'),
        )
    ]

    def get_animal_lobby_song(self, obj):
        return 'https://team-fries-images.s3.us-east-2.amazonaws.com/music/safari-for-lobby.wav'


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


class CapturedSpecialAnimalSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    special_animal = SpecialAnimalSerializer()
    # image = serializers.SerializerMethodField()

    class Meta:
        model = CapturedSpecialAnimal
        fields = (
            'id',
            'owner',
            'special_animal',
            # 'image'

        )

    # def get_image(self, obj):
    #     return obj.special_animal.image.url if obj.special_animal.image else None

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['animal_name'] = representation['special_animal']['animal']['name']
    #     representation['variation_type'] = representation['special_animal']['animal']['variation_type']
    #     del representation['special_animal']
    #     return representation
