from django.urls import path

from qr_kit.views import ReportView, QrCodeView

urlpatterns = [
    path('reports/', ReportView.as_view(), name='report-list'),

    # This serves as a fallback (none of the other routes were hit, so path must be a slug)
    path('<slug:uuid>/', QrCodeView.as_view(), name='qr_code-detail'),
]
