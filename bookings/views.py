from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from restaurants.models import Restaurant
from .models import Booking


@login_required
def book_table(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        date = request.POST.get('date')
        guests = request.POST.get('guests')

        Booking.objects.create(
            user=request.user,
            restaurant=restaurant,
            date=date,
            guests=guests,
        )
        return redirect('restaurant_detail', slug=restaurant.slug)

    return render(request, 'booking.html', {'restaurant': restaurant})
