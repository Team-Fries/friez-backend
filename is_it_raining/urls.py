from django.urls import path
from is_it_raining import views

urlpatterns = [

    path("", views.api_root),

    path("weather-animal/<int:original_code>/",
         views.WeatherAnimalView.as_view(), name="weather-animal"),

    path("list-animals/", views.AnimalListView.as_view(), name="animal-list"),

    path("captured/<str:name>/", views.CapturedAnimalView.as_view(), name="captured"),

    path("my-animals/", views.UserAnimalListView.as_view(), name="my-animals"),

    path("animal-detail/<str:name__iexact>/",
         views.AnimalDetailView.as_view(), name="animal-detail"),

    path('trade/<slug:offered_animal_slug>/<slug:desired_animal_slug>/<str:trade_receiver_username>/',
         views.TradeView.as_view(), name='trade'),

    path('weather-icon/<int:icon_code>',
         views.WeatherIconView.as_view(), name='weather-icon'),

]
