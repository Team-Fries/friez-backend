from django.urls import path
from is_it_raining import views

urlpatterns = [
    path("", views.api_root),
    path("weather-animal/<int:original_code>/",
         views.AnimalDetailView.as_view(), name="weather_animal"),
    path("list-animals/", views.AnimalListView.as_view(), name="animal-list"),
]
