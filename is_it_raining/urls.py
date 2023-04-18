from django.urls import path
from is_it_raining import views

urlpatterns = [
    path("", views.api_root),
    path("weather-animal/<int:weather_code>",
         views.WeatherAnimalView.as_view(), name="weather_animal"),
]
