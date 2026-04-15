from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bookings.models import Booking
from reviews.models import Review
from .models import Dish, Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


@api_view(['GET'])
def api_restaurants(request):
    serializer = RestaurantSerializer(Restaurant.objects.filter(status='published'), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    serializer = RestaurantSerializer(restaurant)
    return Response(serializer.data)


@api_view(['GET'])
def api_dishes(request):
    serializer = DishSerializer(Dish.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_reviews(request):
    serializer = ReviewSerializer(Review.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_bookings(request):
    serializer = BookingSerializer(Booking.objects.all(), many=True)
    return Response(serializer.data)
