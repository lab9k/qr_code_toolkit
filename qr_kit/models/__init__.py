import uuid

from qr_kit.models.fields import JSONField
from django.db import models

from qr_kit.util import HTTP_METHOD_CHOICES, VALUE_TYPE_CHOICES


class InputValue(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=255, choices=VALUE_TYPE_CHOICES)
    parameter_name = models.CharField(max_length=255)
    required = models.BooleanField()

    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='values_to_fill')


class Category(models.Model):
    name = models.CharField(max_length=255)

    endpoint = models.URLField()
    method = models.CharField(max_length=16, choices=HTTP_METHOD_CHOICES)
    success_url = models.URLField(blank=True, null=True)
    redirect_to_form_with_query_params = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Categories"


class QrCode(models.Model):
    uuid = models.CharField(default=uuid.uuid4, editable=True, unique=True, max_length=64)

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='codes', null=True, blank=True)
    values = JSONField(default=dict, blank=True, null=True)


class QrCodeReport(models.Model):
    qr_code = models.ForeignKey(to=QrCode,
                                on_delete=models.SET_NULL,
                                related_name='reports',
                                null=True)
    values = JSONField(default=dict)
