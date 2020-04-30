from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response

from roads_qr_kit.models import Job, TrackedItem
from roads_qr_kit.serializers import JobSerializer, TrackedItemSerializer, JobImageSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    authentication_classes = []

    @action(methods=['post'], detail=True, url_path='add-image', parser_classes=[MultiPartParser])
    def add_image(self, request: Request, pk=None):
        file = request.data['file']
        remark = request.data['remark']
        data = {'stored_image': file, 'job': pk, 'remark': remark}
        serializer = JobImageSerializer(data=data)
        valid = serializer.is_valid()
        if valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = TrackedItemSerializer
    queryset = TrackedItem.objects.all()

    def get_queryset(self):
        only_missing = self.request.query_params.get('missing')
        if only_missing == '1':
            return TrackedItem.objects.filter(missing=True).all()
        else:
            return TrackedItem.objects.all()
