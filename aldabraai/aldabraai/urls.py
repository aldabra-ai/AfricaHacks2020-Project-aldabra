"""
 ROOT URL CONFIGURATION FILE
"""

from django.contrib import admin
from django.urls import (
    path,
    include
)

app_name = 'aldabra.ai'

## API(s) entry points
apis = [
    path('base/', include('base.urls')),
    path('appointments/', include('appointment.urls', namespace='appointments')),
    path('hospitals/', include('hospitaldb.urls', namespace='hospitals')),
    path('accounts/', include('account.urls', namespace='accounts')),
]

urlpatterns = [
    # FRONTEND APP --> DONT PLAY WITH THIS OR WE LOSE OUR NICE DISPLAY 
    path('', include('frontend.urls')),
    # API ENTRY version one --> DONT PLAY WITH THIS OR WE LOSE DATA
    path('api/v1/', include(apis)),
    path('api/auth/', include('authend.urls')),
    path('admin/', admin.site.urls),
]
