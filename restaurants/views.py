from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.http import HttpResponse
from reviews.models import Review
from .models import Restaurant, Dish
from .models import Favorite
from django.db.models import Count
from reviews.models import Review
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Restaurant
from django.views.generic import DetailView
from django.views.generic import CreateView
from .models import Category
from django.urls import reverse_lazy
from django.views.generic import DeleteView



def restaurant_detail(request, slug):
    
    restaurant = Restaurant.objects.get(slug=slug)

    dishes = Dish.objects.filter(restaurant=restaurant)

    reviews = Review.objects.filter(restaurant=restaurant)

    avg_rating = Review.objects.filter(
        restaurant=restaurant
    ).aggregate(Avg("rating"))["rating__avg"]

    return render(request,"restaurant_detail.html",{

        "restaurant":restaurant,

        "dishes":dishes,

        "reviews":reviews,

        "avg_rating":avg_rating

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

def add_favorite(request, restaurant_id):

    restaurant = Restaurant.objects.get(id=restaurant_id)

    Favorite.objects.create(
        user=request.user,
        restaurant=restaurant
    )

    return redirect("profile")

def about(request):
    return HttpResponse("Это страница about")

def home(request):
    return HttpResponse("Главная страница")

def user_profile(request, id):
    return HttpResponse(f"ID пользователя: {id}")

def restaurant_by_slug(request, slug):
    return HttpResponse(f"Ресторан: {slug}")

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def get_home_url(request):
    url = reverse('home')
    return HttpResponse(f"Адрес главной страницы: {url}")

def home_redirect(request):
    return redirect('home')

def numbers_only(request, num):
    return HttpResponse(f"Число: {num}")

def slug_test(request, slug):
    return HttpResponse(f"Slug: {slug}")

def hello(request):
    return HttpResponse("Привет, Django!")

def index(request):
    return render(request, 'index.html', {'name': 'Gulnaz'})

def contact(request):
    message = ""

    if request.method == 'POST':
        message = request.POST.get('message')

    return render(request, 'contact.html', {'message': message})

def contact_redirect(request):
    if request.method == 'POST':
        return redirect('hello')
    return render(request, 'contact_redirect.html')

def json_status(request):
    return JsonResponse({'status': 'ok'})

class AboutPageView(TemplateView):
    template_name = 'about.html'

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail_view.html'
    context_object_name = 'restaurant'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy('hello')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('hello')