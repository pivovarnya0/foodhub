from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg, Q
from django.shortcuts import get_object_or_404, redirect, render

from bookings.models import Booking
from reviews.models import Review
from .models import Category, Favorite, Restaurant


def home(request):
    query = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '').strip()

    restaurants = Restaurant.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    if query:
        restaurants = restaurants.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )

    if category_id:
        restaurants = restaurants.filter(category_id=category_id)

    paginator = Paginator(restaurants, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = list(
            Favorite.objects.filter(user=request.user).values_list('restaurant_id', flat=True)
        )

    return render(request, 'home.html', {
        'page_obj': page_obj,
        'query': query,
        'categories': categories,
        'selected_category': category_id,
        'favorite_ids': favorite_ids,
    })


def restaurant_detail(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    dishes = restaurant.dishes.all()
    reviews = Review.objects.filter(restaurant=restaurant).order_by('-created_at')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(user=request.user, restaurant=restaurant).exists()

    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'dishes': dishes,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'is_favorite': is_favorite,
    })


@login_required
def add_favorite(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, restaurant=restaurant)

    if not created:
        favorite.delete()
        messages.success(request, 'Removed from favorites.')
    else:
        messages.success(request, 'Added to favorites.')

    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def remove_favorite(request, restaurant_id):
    Favorite.objects.filter(user=request.user, restaurant_id=restaurant_id).delete()
    messages.success(request, 'Restaurant removed from favorites.')
    return redirect('profile')


def custom_404(request, exception):
    return render(request, '404.html', status=404)
