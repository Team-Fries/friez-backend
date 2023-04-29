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
    audio_file = models.FileField(blank=True, null=True,
                                  upload_to='music')

    def __str__(self):
        return self.name


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


class CapturedAnimal(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner')
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='animal')
    last_capture_date = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    capture_count = models.PositiveIntegerField(default=1)
    points = models.PositiveIntegerField(default=1)

    def get_points(self):
        return self.points

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['owner', 'animal'], name='unique_ownership')
        ]

    def __str__(self):
        return f"{self.owner} captured {self.animal} ({self.points} points)"


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


class SpecialAnimal(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name='special_animal')
    image = models.ImageField(blank=True, null=True,
                              upload_to='team-fries-images')

    def __str__(self):
        return f"{self.animal.name} {self.animal.variation_type}"


class CapturedSpecialAnimal(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='special_owner')
    special_animal = models.ForeignKey(
        SpecialAnimal, on_delete=models.CASCADE, related_name='special_animal')

    def __str__(self):
        return f"{self.owner} unlocked {self.special_animal.animal.name} {self.special_animal.animal.variation_type}"
