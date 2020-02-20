from rest_framework import routers
from roads_qr_kit import viewsets

router = routers.DefaultRouter()
router.register(r'job', viewsets.JobViewSet)
router.register(r'item', viewsets.ItemViewSet)

urlpatterns = router.urls
