from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from bookings.models import Booking
from restaurants.models import Favorite
from reviews.models import Review
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def profile_view(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('restaurant')
    reviews = Review.objects.filter(user=request.user)
    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'profile.html', {
        'favorites': favorites,
        'reviews': reviews,
        'bookings': bookings,
    })
