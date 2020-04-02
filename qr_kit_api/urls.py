from django.urls import path
from rest_framework import routers

from qr_kit_api.views import CodeExistsView
from qr_kit_api.viewsets import CategoryViewSet, QrCodeViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('code', QrCodeViewSet)

urlpatterns = router.urls
urlpatterns = urlpatterns + [
    path('exists/<slug:uuid>/', CodeExistsView.as_view(), name='code-exists')
]
