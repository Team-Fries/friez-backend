from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=3, decimal_places=0)
    description = models.CharField()
    icon = models.CharField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
