from django.urls import path
from . import views
from . import api

urlpatterns = [

    path("", views.home, name="home"),

    path("restaurant/<slug:slug>/", views.restaurant_detail, name="restaurant_detail"),

    path("statistics/", views.statistics, name="statistics"),

    # API
    path("api/restaurants/", api.api_restaurants),
    path("api/restaurants/<int:id>/", api.api_restaurant_detail),
    path("api/dishes/", api.api_dishes),
    path("api/reviews/", api.api_reviews),
    path("api/bookings/", api.api_bookings),
    path("favorite/<int:restaurant_id>/", views.add_favorite, name="favorite"),
]