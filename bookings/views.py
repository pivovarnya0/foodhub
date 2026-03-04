from django.shortcuts import render, redirect
from .models import Booking
from restaurants.models import Restaurant
from django.contrib.auth.decorators import login_required

@login_required
def book_table(request, restaurant_id):

    restaurant = Restaurant.objects.get(id=restaurant_id)

    if request.method == 'POST':
        date = request.POST.get('date')
        guests = request.POST.get('guests')

        Booking.objects.create(
            user=request.user,
            restaurant=restaurant,
            date=date,
            guests=guests
        )

        return redirect('/')

    return render(request, 'booking.html', {'restaurant': restaurant})