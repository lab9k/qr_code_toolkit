from rest_framework.response import Response
from rest_framework.views import APIView

from qr_kit.models import QrCode


class CodeExistsView(APIView):
    def get(self, request, uuid=None, format=None):

        if uuid is None:
            return Response({
                'exists': False
            })

        if QrCode.objects.filter(uuid=uuid).exists():
            return Response({
                'exists': True
            })
        else:
            return Response({
                'exists': False
            })
