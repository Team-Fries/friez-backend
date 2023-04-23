from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Weather(models.Model):
    weather_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.weather_code)


class WeatherIcon(models.Model):
    icon_code = models.IntegerField(blank=True, null=True)
    icon_image = models.ImageField(blank=True, null=True,
                                   upload_to='weather-icons')


class Animal(models.Model):
    name = models.CharField(max_length=100)
    weather = models.ForeignKey(
        Weather, on_delete=models.CASCADE, related_name='weather_type_for_animal')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


# creating related image model so each animal can have multiple images
class AnimalImage(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True, null=True,
                              upload_to='team-fries-images')

    def __str__(self):
        return f"Image for {self.animal}"


class CapturedAnimal(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner')
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='animal')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'animal'], name='unique_ownership')
        ]

    def __str__(self):
        return f"{self.owner} captured {self.animal}"


class Trade(models.Model):

    TRADE_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    )

    trade_starter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='initiated_trades')
    trade_receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_trades')
    offered_animal = models.ForeignKey(
        CapturedAnimal, on_delete=models.CASCADE, related_name='offered_in_trades')
    desired_animal = models.ForeignKey(
        CapturedAnimal, on_delete=models.CASCADE, related_name='desired_in_trades')
    status = models.CharField(
        choices=TRADE_STATUS_CHOICES, default='pending', max_length=20)

    def __str__(self):
        return f"{self.offered_animal} - EXCHANGED FOR: {self.desired_animal}"
