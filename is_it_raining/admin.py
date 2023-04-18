from django.contrib import admin
from .models import User, Animal, Weather

admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Weather)
