from django.urls import reverse
from rest_framework import serializers

from qr_kit.models import InputValue, Category, QrCode


class InputValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputValue
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    values_to_fill = InputValueSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = '__all__'


class QrCodeSerializer(serializers.HyperlinkedModelSerializer):
    values = serializers.JSONField()
    scan_url = serializers.HyperlinkedIdentityField(view_name='qr_code-detail', lookup_url_kwarg='uuid',
                                                    lookup_field='uuid', read_only=True)

    class Meta:
        model = QrCode
        fields = ('id', 'values', 'scan_url', 'uuid', 'category', 'url')
        read_only_fields = ['uuid', 'id', 'scan_url', 'url']
