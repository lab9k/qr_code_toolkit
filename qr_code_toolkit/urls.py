from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views

from jobqr.urls import router as oldRouter
from roads_qr_kit.views import QrCodeView

from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include([
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ])),
    path('old/', include('jobqr.urls')),
    path('old/api/', include(oldRouter.urls)),
    path('code/<int:pk>/', QrCodeView.as_view(), name='qr_code_public'),
    path('api/v2/', include('roads_qr_kit.urls')),
    path('api/v3/', include('qr_kit_api.urls')),
    path('', include('qr_kit.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
