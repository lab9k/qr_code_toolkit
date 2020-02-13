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

    @property
    def is_instant_redirect(self) -> bool:
        # TODO: define this property
        return False

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Categories"


class QrCode(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='codes')
    values = JSONField(default=dict)
