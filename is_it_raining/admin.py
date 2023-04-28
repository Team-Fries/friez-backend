from django.contrib import admin
from .models import User, Animal, Weather, CapturedAnimal, Trade, Background, SpecialAnimal, CapturedSpecialAnimal

admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Weather)
admin.site.register(CapturedAnimal)
admin.site.register(Trade)
admin.site.register(Background)
admin.site.register(SpecialAnimal)
admin.site.register(CapturedSpecialAnimal)
