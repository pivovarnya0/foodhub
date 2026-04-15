from django.urls import path
from . import api, views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/<slug:slug>/', views.restaurant_detail, name='restaurant_detail'),
    path('favorite/<int:restaurant_id>/', views.add_favorite, name='favorite'),
    path('favorite/remove/<int:restaurant_id>/', views.remove_favorite, name='remove_favorite'),

    path('api/restaurants/', api.api_restaurants, name='api_restaurants'),
    path('api/restaurants/<int:id>/', api.api_restaurant_detail, name='api_restaurant_detail'),
    path('api/dishes/', api.api_dishes, name='api_dishes'),
    path('api/reviews/', api.api_reviews, name='api_reviews'),
    path('api/bookings/', api.api_bookings, name='api_bookings'),
]
