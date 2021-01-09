from .api import views
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register('site_info', views.StaticSiteInfoViewSet, basename='site-info')
router.register('features', views.FeatureViewSet, basename='features')
router.register('sponsors', views.SponsorViewSet, basename='sponsors')

urlpatterns = router.urls