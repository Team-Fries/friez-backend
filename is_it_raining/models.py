from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Weather(models.Model):
    # temp = models.DecimalField(max_digits=3, decimal_places=0)
    weather_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.temp


class Animal(models.Model):
    name = models.CharField(max_length=100)
    weather = models.ForeignKey(
        Weather, on_delete=models.CASCADE, related_name='weather_type_for_animal')
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='animals_of_owner')

    def __str__(self):
        return self.name
