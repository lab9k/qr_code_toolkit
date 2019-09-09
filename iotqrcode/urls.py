from django.urls import path
from iotqrcode.views import DeviceView, DeviceListView, DeviceQRView, DeviceQRListView

urlpatterns = [
    path('', DeviceListView.as_view(), name='home'),
    path('device/<int:id>/', DeviceView.as_view(), name='device_detail'),
    path('qr/', DeviceQRListView.as_view(), name='device_qr_list'),
    path('qr/<int:id>/', DeviceQRView.as_view(), name='device_qr'),
]
