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
    class Meta:
        model = QrCode
        fields = '__all__'
