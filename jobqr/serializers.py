from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from jobqr.models import TrackedItem, Job


class TrackedItemSerializer(ModelSerializer):
    class Meta:
        model = TrackedItem
        fields = ['name', 'location', 'is_in_use', 'job', 'pk']


class JobSerializer(ModelSerializer):
    current_items = TrackedItemSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
