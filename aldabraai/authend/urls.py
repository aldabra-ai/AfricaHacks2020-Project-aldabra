# django COMMON
from django.urls import path

# KNOX
from knox import views as knox_views

# API
from .api import LoginView

urlpatterns = [
     path('login/', LoginView.as_view(), name='knox_login'),
     path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]