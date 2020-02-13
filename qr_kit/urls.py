from rest_framework import routers
from django.urls import path

from qr_kit.viewsets import CategoryViewSet, QrCodeViewSet
from qr_kit import views

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('code', QrCodeViewSet)

urlpatterns = router.urls
