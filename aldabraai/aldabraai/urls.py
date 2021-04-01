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
    path('hospitaldb/', include('hospitaldb.urls', namespace='hospitaldb')),
    path('accounts/', include('account.urls', namespace='accounts')),
]

urlpatterns = [
    # FRONTEND APP --> DONT PLAY WITH THIS OR WE LOSE OUR NICE DISPLAY 
    path('', include('frontend.urls')),
    # API ENTRY version one --> DONT PLAY WITH THIS OR WE LOSE DATA
    path('api/v1/', include(apis)),
    path('admin/', admin.site.urls),
]
