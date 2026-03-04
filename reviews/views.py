from django.shortcuts import render, redirect
from .models import Review
from restaurants.models import Restaurant
from django.contrib.auth.decorators import login_required

@login_required
def add_review(request, restaurant_id):

    restaurant = Restaurant.objects.get(id=restaurant_id)

    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Review.objects.create(
            user=request.user,
            restaurant=restaurant,
            rating=rating,
            comment=comment
        )

        return redirect(f"/restaurant/{restaurant.id}/")

    return render(request, "add_review.html", {"restaurant": restaurant})