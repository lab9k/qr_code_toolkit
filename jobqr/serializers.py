from rest_framework.serializers import ModelSerializer, SerializerMethodField
from jobqr.models import TrackedItem, Job
from reversion.models import Version


class VersionSerializer(ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'


class TrackedItemSerializer(ModelSerializer):
    history = SerializerMethodField(method_name='get_history')

    # noinspection PyMethodMayBeStatic
    def get_history(self, obj):
        serializer = VersionSerializer(obj.get_history(), many=True)
        return serializer.data

    class Meta:
        model = TrackedItem
        fields = ['name', 'location', 'is_in_use', 'job', 'pk', 'last_update', 'history', 'missing']


class JobSerializer(ModelSerializer):
    current_items = TrackedItemSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
