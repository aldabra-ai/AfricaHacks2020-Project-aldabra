## REST FRAMEWORK IMPORTS
from rest_framework import routers

## API Views
from .api import (
    DoctorOfficeAPI,
    DoctorOfficeScheduleAPI
)


app_name = 'hospitals'

router = routers.DefaultRouter()
router.register('offices', DoctorOfficeAPI, basename='offices')
router.register('schedules', DoctorOfficeScheduleAPI, basename='schedules')

urlpatterns = router.urls
