from django.urls import path
# from .views import staticinfolist, staticinfo_detail
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import LandingPage

app_name = 'baseapp'

urlpatterns = [
    path('', LandingPage.as_view(), name='landing-page')
    # path('staticinfos/', staticinfolist),
    # path('staticinfo_detail/<int:pk>/', staticinfo_detail)
]

#urlpatterns = format_suffix_patterns(urlpatterns)