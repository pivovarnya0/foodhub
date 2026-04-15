from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from users.forms import CustomLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('restaurants.urls')),
    path('', include('bookings.urls')),
    path('', include('reviews.urls')),
    path('', include('users.urls')),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html',
            authentication_form=CustomLoginForm
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

handler404 = 'restaurants.views.custom_404'
