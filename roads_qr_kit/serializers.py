import json
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from reversion.models import Version

from roads_qr_kit.models import TrackedItem, Job, JobImage


class VersionSerializer(serializers.ModelSerializer):
    serialized_data = serializers.SerializerMethodField(method_name='get_serialized_data', read_only=True)

    # noinspection PyMethodMayBeStatic
    def get_serialized_data(self, obj):
        return json.loads(obj.serialized_data)

    class Meta:
        model = Version
        fields = '__all__'


class TrackedItemSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField(method_name='get_history', read_only=True)
    item_id = serializers.IntegerField(read_only=True)
    qr_payload = serializers.HyperlinkedIdentityField('qr_code_public', read_only=True)

    # noinspection PyMethodMayBeStatic
    def get_history(self, obj):
        serializer = VersionSerializer(obj.get_history(), many=True)
        return serializer.data

    class Meta:
        model = TrackedItem
        fields = '__all__'


class RegisterItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)

    # noinspection PyMethodMayBeStatic
    def validate_item_id(self, item_id):
        if len(TrackedItem.objects.filter(item_id=item_id)) > 0:
            raise ValidationError(detail='This item is already registered')
        return item_id

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return TrackedItem.objects.create(**validated_data)


class JobImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobImage
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    current_items = TrackedItemSerializer(many=True, required=False)
    images = JobImageSerializer(many=True, required=False)
    url = serializers.HyperlinkedIdentityField(view_name='job-detail')

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('id',)
