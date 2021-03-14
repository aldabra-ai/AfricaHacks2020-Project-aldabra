from rest_framework import routers
# #from .api.views import DoctorOfficeAPI


app_name = 'hospitaldb'

router = routers.DefaultRouter()
# router.register('doctor-office', DoctorOfficeAPI, basename='doctoroffice')

urlpatterns = router.urls