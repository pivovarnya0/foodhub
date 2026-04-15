from django.contrib.auth.models import User
from django.db import models
from restaurants.models import Restaurant


class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    guests = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} booking at {self.restaurant.name}'
