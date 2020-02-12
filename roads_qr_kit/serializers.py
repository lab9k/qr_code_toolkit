from rest_framework import serializers
from reversion.models import Version

from roads_qr_kit.models import TrackedItem, Job, JobImage


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'


class TrackedItemSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField(method_name='get_history')
    item_id = serializers.IntegerField(read_only=True)

    # noinspection PyMethodMayBeStatic
    def get_history(self, obj):
        serializer = VersionSerializer(obj.get_history(), many=True)
        return serializer.data

    class Meta:
        model = TrackedItem
        fields = '__all__'


class JobImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobImage
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    current_items = TrackedItemSerializer(many=True, required=False)
    images = JobImageSerializer(many=True, required=False)

    class Meta:
        model = Job
        fields = '__all__'
