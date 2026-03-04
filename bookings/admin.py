from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ("user", "restaurant", "date", "guests")

    list_filter = ("restaurant",)