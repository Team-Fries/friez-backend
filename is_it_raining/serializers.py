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
    images = serializers.SlugRelatedField(
        read_only=True, many=True, slug_field='image')
    random_image = serializers.SerializerMethodField()

    class Meta:
        model = Animal
        fields = (
            'id',
            'name',
            'weather',
            'images',
            'random_image'
        )

    def get_random_image(self, obj):
        image = obj.images.order_by("?").first()
        return image


class AnimalImageSerializer(serializers.ModelSerializer):
    model = AnimalImage
    fields = (
        'id',
        'animal',
        'image'
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
