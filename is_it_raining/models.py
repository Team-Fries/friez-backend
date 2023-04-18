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

    def __str__(self):
        return self.name
