from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from jobqr.urls import router as oldRouter
from qr_kit.views import QrCodeView, ReportView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include([
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ])),
    path('old/', include('jobqr.urls')),
    path('old/api/', include(oldRouter.urls)),
    path('', RedirectView.as_view(url='/api/v3', permanent=False)),
    path('api/v2/', include('roads_qr_kit.urls')),
    path('api/v3/', include('qr_kit.urls')),
    path('reports/', ReportView.as_view(), name='report-list'),
    path('<slug:uuid>/', QrCodeView.as_view(), name='qr_code-detail')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
