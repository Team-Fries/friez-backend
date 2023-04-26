from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Weather(models.Model):
    weather_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.weather_code)


class Background(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    background_image = models.ImageField(blank=True, null=True,
                                         upload_to='background')
    code = models.CharField(max_length=3)
    day_or_night = models.CharField(max_length=2)

    def __str__(self):
        return self.name


# class WeatherIcon(models.Model):
#     icon_code = models.IntegerField(blank=True, null=True)
#     icon_image = models.ImageField(blank=True, null=True,
#                                    upload_to='weather-icons')
#     is_day = models.BooleanField(null=True)


class Animal(models.Model):

    VARIATION_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )

    name = models.CharField(max_length=100)
    weather = models.ForeignKey(
        Weather, on_delete=models.CASCADE, related_name='weather_type_for_animal')
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    variation_type = models.CharField(
        choices=VARIATION_CHOICES, default='A', max_length=20)
    image = models.ImageField(blank=True, null=True,
                              upload_to='team-fries-images')

    def __str__(self):
        return f"{self.name} - type: {self.variation_type}"


# creating related image model so each animal can have multiple images
# class AnimalImage(models.Model):
#     animal = models.ForeignKey(
#         Animal, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(blank=True, null=True,
#                               upload_to='team-fries-images')

#     def __str__(self):
#         return f"Image for {self.animal}"


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
