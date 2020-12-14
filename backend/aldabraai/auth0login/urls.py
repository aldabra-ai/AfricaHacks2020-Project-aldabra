from django.urls import path, include
from .views import login_view, logout


urlpatterns = [
    path('', login_view),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
    path('logout', logout, name='logout'),
]