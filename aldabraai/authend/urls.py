# django COMMON
from collections import namedtuple
from django.urls import path

# KNOX
from knox import views as knox_views

# API
from .api import (
     #SignUpAPIView,
     LoginAPIView,
)

# VIEWS
from .views import (
     registrationView,
     onboardingPath,
     userLoginView,
     logout_view
)

urlpatterns = [
     ## auth api level url endpoints
     #path('signup/', SignUpAPIView.as_view(), name='api_signup'),
     path('login_api/', LoginAPIView.as_view(), name='knox_login'),
     path('logout_api/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path('logoutall_api/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),

     ## app app level urls
     path('signup/', registrationView, name='signup'),
     path('onboard-path/', onboardingPath, name='user_path'),
     path('login/', userLoginView, name='login'),
     path('logout/', logout_view, name='logout')

]