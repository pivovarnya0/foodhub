from django.urls import path
from . import views

urlpatterns = [
    path('booking/<int:restaurant_id>/', views.book_table, name='booking'),
]