from django.urls import path
from jobqr.views import JobListView, JobView, RegisterView, HomeView, ItemDetailView, MapView, HistoryView
from rest_framework.routers import DefaultRouter
from jobqr.viewsets import ItemViewSet, JobViewSet, untrack, report_missing

router = DefaultRouter()
router.register(r'device', ItemViewSet)
router.register(r'job', JobViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('job/', JobListView.as_view(), name='job_list'),
    path('job/<int:pk>/', JobView.as_view(), name='job_detail'),
    path('job/<int:pk>/untrack/<int:item_pk>/', untrack, name='untrack'),
    path('register/', RegisterView.as_view(), name='register'),
    path('device/<int:pk>/', ItemDetailView.as_view(), name='device_detail'),
    path('device/<int:pk>/missing/', report_missing, name='report_missing'),
    path('device/<int:pk>/history/', HistoryView.as_view(), name='device_history'),
    path('map/', MapView.as_view(), name='map')
]
