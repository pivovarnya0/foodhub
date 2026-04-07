from django.urls import path
from . import views
from . import api
from django.urls import path
from .views import restaurant_by_slug
from .views import slug_test
from django.urls import path
from .views import hello
from .views import hello, index
from .views import hello, index, contact
from .views import hello, index, contact, contact_redirect
from .views import hello, index, contact, contact_redirect, json_status
from .views import hello, index, contact, contact_redirect, json_status, AboutPageView
from .views import RestaurantListView
from .views import RestaurantDetailView
from .views import CategoryCreateView
from .views import CategoryDeleteView


urlpatterns = [

    path("", views.home, name="home"),

    path("restaurant/<slug:slug>/", views.restaurant_detail, name="restaurant_detail"),

    path("statistics/", views.statistics, name="statistics"),

    # API
    path("api/restaurants/", api.api_restaurants),
    path("api/restaurants/<int:id>/", api.api_restaurant_detail),
    path("api/dishes/", api.api_dishes),
    path("api/reviews/", api.api_reviews),
    path("api/bookings/", api.api_bookings),
    path("favorite/<int:restaurant_id>/", views.add_favorite, name="favorite"),
    path('restaurant/<slug:slug>/', restaurant_by_slug, name='restaurant_slug'),
    path('slug-test/<slug:slug>/', slug_test, name='slug_test'),
    path('hello/', hello, name='hello'),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'),
    path('contact-redirect/', contact_redirect, name='contact_redirect'),
    path('json-status/', json_status, name='json_status'),
    path('about-page/', AboutPageView.as_view(), name='about_page'),
    path('restaurant-list/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurant-detail/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail_view'),
    path('category-add/', CategoryCreateView.as_view(), name='category_add'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]