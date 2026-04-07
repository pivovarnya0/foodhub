from django.contrib import admin
from .models import Restaurant, Category, Dish, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DishInline(admin.TabularInline):
    model = Dish


def make_published(modeladmin, request, queryset):
    queryset.update(status='published')
make_published.short_description = "Сделать опубликованными"


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status')
    search_fields = ('name',)
    list_filter = ('category', 'status')
    inlines = [DishInline]
    actions = [make_published]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.site_header = "FoodHub Admin"
admin.site.site_title = "Админка FoodHub"
admin.site.index_title = "Панель управления FoodHub"