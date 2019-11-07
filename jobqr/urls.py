from django.urls import path
from jobqr.views import JobListView, JobView, RegisterView, HomeView
from rest_framework.routers import DefaultRouter
from jobqr.viewsets import ItemViewSet, JobViewSet, untrack

router = DefaultRouter()
router.register(r'item', ItemViewSet)
router.register(r'job', JobViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('job/', JobListView.as_view(), name='job_list'),
    path('job/<int:pk>/', JobView.as_view(), name='job_detail'),
    path('job/<int:pk>/untrack/<int:item_pk>/', untrack, name='untrack'),
    path('register/', RegisterView.as_view(), name='register')
]
