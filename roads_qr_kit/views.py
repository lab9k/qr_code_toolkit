from rest_framework import generics

from roads_qr_kit.models import TrackedItem
from roads_qr_kit.serializers import RegisterItemSerializer


class RegisterView(generics.CreateAPIView):
    queryset = TrackedItem.objects.all()
    serializer_class = RegisterItemSerializer
