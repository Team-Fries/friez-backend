from django.contrib import admin
from .models import User, Animal, Weather, CapturedAnimal, AnimalImage

admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Weather)
admin.site.register(CapturedAnimal)
admin.site.register(AnimalImage)
