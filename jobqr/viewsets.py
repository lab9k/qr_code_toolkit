from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from jobqr.models import TrackedItem, Job
from jobqr.serializers import TrackedItemSerializer, JobSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


class ItemViewSet(ModelViewSet):
    queryset = TrackedItem.objects.all()
    serializer_class = TrackedItemSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


@require_http_methods(['POST'])
def untrack(request, pk, item_pk):
    item = TrackedItem.objects.get(item_id=item_pk)
    job = Job.objects.get(pk=pk)
    if item is not None:
        if item.job.pk == pk:
            item.is_in_use = False
            item.job = None
            item.save()
            serializer = JobSerializer(job)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({'error': 'Item was not registered to this job'},
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'item cannot be found'}, status=status.HTTP_400_BAD_REQUEST)
