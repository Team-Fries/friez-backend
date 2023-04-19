from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Weather(models.Model):
    weather_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.weather_code)


class Animal(models.Model):
    name = models.CharField(max_length=100)
    weather = models.ForeignKey(
        Weather, on_delete=models.CASCADE, related_name='weather_type_for_animal')
    # adding an image attribute that will upload from AWS storage
    image = models.ImageField(blank=True, null=True,
                              upload_to='team-fries-images')
    # ?? use URLFiled(null=True) instead??

    def __str__(self):
        return self.name
