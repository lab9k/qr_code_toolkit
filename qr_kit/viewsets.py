from rest_framework import viewsets

from qr_kit.models import Job, TrackedItem
from qr_kit.serializers import JobSerializer, TrackedItemSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = TrackedItemSerializer
    queryset = TrackedItem.objects.all()

    def get_queryset(self):
        only_missing = self.request.query_params.get('missing')
        if only_missing == '1':
            return TrackedItem.objects.filter(missing=True)
        else:
            return TrackedItem.objects.all()
