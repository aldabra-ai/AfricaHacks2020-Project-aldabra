"""
 ROOT URL CONFIGURATION FILE
"""

from django.contrib import admin
from django.urls import path, include

## API(s) entry points
apis = [
    path('base/', include('base.urls')),
    path('appointment/', include('appointment.urls', namespace='appointment')),
    path('hospitaldb/', include('hospitaldb.urls', namespace='hospitaldb')),
    path('accounts/', include('account.urls', namespace='accounts')),
]

urlpatterns = [
    path('', include('frontend.urls')),
    path('api/', include(apis)),
    path('admin/', admin.site.urls),
]
