"""
 ROOT URL CONFIGURATION FILE
"""

from django.contrib import admin
from django.urls import (
    path,
    include
)

## API(s) entry points
apis = [
    path('base/', include('base.urls')),
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('hospitaldb/', include('hospitaldb.urls', namespace='hospitaldb')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

urlpatterns = [
    # FRONTEND APP --> DONT PLAY WITH THIS OR WE LOSE OUR NICE DISPLAY 
    path('', include('frontend.urls')),
    # API ENTRY version one --> DONT PLAY WITH THIS OR WE LOSE DATA
    path('apis/v1/', include(apis)),
    path('admin/', admin.site.urls),
]
