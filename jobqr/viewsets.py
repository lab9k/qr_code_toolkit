from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from jobqr.models import TrackedItem, Job
from jobqr.serializers import TrackedItemSerializer, JobSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


class ItemViewSet(ModelViewSet):
    serializer_class = TrackedItemSerializer
    queryset = TrackedItem.objects.all()

    def get_queryset(self):
        only_missing = self.request.query_params.get('missing')
        if only_missing == '1':
            return TrackedItem.objects.filter(missing=True)
        else:
            return TrackedItem.objects.all()


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


@require_http_methods(['POST'])
def report_missing(request, pk):
    item = TrackedItem.objects.get(item_id=pk)
    if item is not None:
        item.missing = not item.missing
        item.save()
        serializer = TrackedItemSerializer(item)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({'error': 'item cannot be found'}, status=status.HTTP_400_BAD_REQUEST)
