from django.db import models
from django.urls import reverse
from location_field.models.plain import PlainLocationField


# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False, default='Ghent')
    location = PlainLocationField(based_fields=['location'])

    def get_absolute_url(self):
        return reverse("device_detail", kwargs={'id': self.pk})
