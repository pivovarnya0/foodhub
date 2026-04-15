from django.contrib import admin
from .models import Category, Dish, Favorite, Restaurant, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class DishInline(admin.TabularInline):
    model = Dish
    extra = 1


def make_published(modeladmin, request, queryset):
    queryset.update(status='published')


make_published.short_description = 'Make selected restaurants published'


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'status', 'created_at')
    list_filter = ('category', 'status')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [DishInline]
    actions = [make_published]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'restaurant', 'created')
    list_filter = ('created',)
    readonly_fields = ('created',)


admin.site.site_header = 'FoodHub Admin'
admin.site.site_title = 'FoodHub Admin Panel'
admin.site.index_title = 'Welcome to FoodHub Administration'
