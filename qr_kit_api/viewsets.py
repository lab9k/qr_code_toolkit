from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from qr_kit.models import Category, InputValue, QrCode
from qr_kit_api.serializers import CategorySerializer, InputValueSerializer, QrCodeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QrCodeViewSet(viewsets.ModelViewSet):
    queryset = QrCode.objects.all()
    serializer_class = QrCodeSerializer
    lookup_field = 'uuid'

    @action(detail=True, methods=['get'])
    def exists(self, request, uuid=None):
        code = self.get_object()
        if code is not None:
            return Response({'exists': True})
        else:
            return Response({'exists': False})
