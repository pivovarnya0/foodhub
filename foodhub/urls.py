from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from restaurants.views import home
from restaurants.views import user_profile
from restaurants.views import get_home_url
from restaurants.views import home_redirect
from django.urls import re_path
from restaurants.views import numbers_only

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('restaurants.urls')),
    path('admin/', admin.site.urls),
    path('', include('restaurants.urls')),
    path('', include('bookings.urls')),
    path('', include('reviews.urls')),
    path('', include('users.urls')),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),  
    path('', home, name='home'),
    path('user/<int:id>/', user_profile),
    path('', include('restaurants.urls')),
    path('get-home-url/', get_home_url),
    path('home/', home_redirect),
    re_path(r'^numbers/(?P<num>[0-9]+)/$', numbers_only),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'restaurants.views.custom_404'