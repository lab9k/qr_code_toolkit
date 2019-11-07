from django.urls import path
from register.views import register_item

urlpatterns = [
    path('', register_item, name='register-code')
]
