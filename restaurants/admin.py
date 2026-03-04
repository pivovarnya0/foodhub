from django.contrib import admin
from .models import Restaurant, Category, Dish


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    list_display = ("name", "category")

    search_fields = ("name",)

    list_filter = ("category",)

    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name",)

    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_display = ("name", "restaurant", "price")

    search_fields = ("name",)

    list_filter = ("restaurant",)