from django.urls import path
from rest_framework import routers
from roads_qr_kit import viewsets
from roads_qr_kit.views import RegisterView

router = routers.DefaultRouter()
router.register(r'job', viewsets.JobViewSet)
router.register(r'item', viewsets.ItemViewSet)

urlpatterns = [path('item/register/', RegisterView.as_view(), name='register-item'), ]
urlpatterns += router.urls
