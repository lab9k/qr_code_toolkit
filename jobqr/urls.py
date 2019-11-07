from django.urls import path
from jobqr.views import JobListView, JobView
from rest_framework.routers import DefaultRouter
from jobqr.viewsets import ItemViewSet, JobViewSet, untrack

router = DefaultRouter()
router.register(r'item', ItemViewSet)
router.register(r'job', JobViewSet)

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('<int:pk>/', JobView.as_view(), name='job_detail'),
    path('<int:pk>/untrack/<int:item_pk>/', untrack, name='untrack')
]
