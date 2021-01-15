"""
 ROOT URL CONFIGURATION FILE
"""

from django.contrib import admin
from django.urls import path, include

## API(s) entry points
apis = [
    path('base/', include('base.urls')),
]

urlpatterns = [
    path('', include('frontend.urls')),
    path('api/', include(apis)),
    path('admin/', admin.site.urls),
]
