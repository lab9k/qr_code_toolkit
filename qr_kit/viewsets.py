from rest_framework import viewsets

from qr_kit.models import Category, InputValue, QrCode
from qr_kit.serializers import CategorySerializer, InputValueSerializer, QrCodeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QrCodeViewSet(viewsets.ModelViewSet):
    queryset = QrCode.objects.all()
    serializer_class = QrCodeSerializer
