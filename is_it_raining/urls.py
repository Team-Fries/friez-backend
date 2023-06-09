from django.urls import path
from is_it_raining import views

urlpatterns = [

    path("", views.api_root),

    path("weather-animal/<int:original_code>/",
         views.WeatherAnimalView.as_view(), name="weather-animal"),

    path("list-animals/", views.AnimalListView.as_view(), name="animal-list"),

    path("captured/<str:name>/<str:variation>/",
         views.CapturedAnimalView.as_view(), name="captured"),

    path("my-animals/", views.UserAnimalListView.as_view(), name="my-animals"),

    path("my-special-animals/", views.UserSpecialAnimalListView.as_view(),
         name="my-special-animals"),

    path('animal-detail/<str:name>/<str:variation_type>/',
         views.AnimalDetailView.as_view(), name='animal-detail'),

    path('trade/', views.TradeView.as_view(), name='trade'),

    path('my-offers/', views.MyTradeOfferView.as_view(), name='my-offers'),

    path('my-received-offers/', views.MyReceivedOfferView.as_view(),
         name='my-received-offers'),

    path('trade/accept/<int:trade_id>/',
         views.TradeAcceptView.as_view(), name='trade-accept'),

    path('background/', views.BackgroundView.as_view(), name='background'),

]
