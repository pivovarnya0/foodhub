from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from restaurants.models import Restaurant
from .models import Review


@login_required
def add_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        Review.objects.create(
            user=request.user,
            restaurant=restaurant,
            rating=rating,
            comment=comment,
        )
        return redirect('restaurant_detail', slug=restaurant.slug)

    return render(request, 'add_review.html', {'restaurant': restaurant})
