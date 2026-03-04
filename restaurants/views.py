from django.shortcuts import render
from django.core.paginator import Paginator

from reviews.models import Review
from .models import Restaurant, Dish

from django.db.models import Count
from reviews.models import Review

def restaurant_detail(request, slug):

    restaurant = Restaurant.objects.get(slug=slug)

    dishes = Dish.objects.filter(restaurant=restaurant)

    reviews = Review.objects.filter(restaurant=restaurant)

    return render(request,"restaurant_detail.html",{

        "restaurant":restaurant,

        "dishes":dishes,

        "reviews":reviews

    })

from django.shortcuts import render
from .models import Restaurant

from django.db.models import Q

def home(request):

    query = request.GET.get("q")

    restaurants = Restaurant.objects.all()

    if query:
        restaurants = restaurants.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    paginator = Paginator(restaurants,6)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request,"home.html",{

        "page_obj":page_obj

    })

def statistics(request):

    stats = Restaurant.objects.annotate(

        review_count=Count("review")

    )

    return render(request,"statistics.html",{

        "stats":stats

    })