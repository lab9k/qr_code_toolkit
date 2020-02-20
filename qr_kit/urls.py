from rest_framework import routers
from qr_kit.viewsets import CategoryViewSet, QrCodeViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('code', QrCodeViewSet)

urlpatterns = router.urls
