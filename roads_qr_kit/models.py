from django.db import models

from location_field.models.plain import PlainLocationField
from reversion.models import Version
import requests


class Job(models.Model):
    name = models.CharField(max_length=255)
    order_number = models.BigIntegerField()
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=128, default='')

    def save(self, *args, **kwargs):
        url_address = self.address.replace(' ', '+')
        data = requests.get(
            f'https://nominatim.openstreetmap.org/?q={url_address}&format=json&limit=1&country=Belgium').json()
        lat = data[0]['lat']
        lon = data[0]['lon']
        self.location = f'{lat},{lon}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class JobImage(models.Model):
    stored_image = models.ImageField(upload_to='img/jobs/')
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=255, blank=True, default='')


class TrackedItem(models.Model):
    item_id = models.AutoField(
        primary_key=True,
    )
    job = models.ForeignKey(to='Job',
                            on_delete=models.SET_NULL,
                            blank=True,
                            null=True,
                            related_name='current_items')
    name = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['location'],
                                  default='51.0538286,3.7250121')
    is_in_use = models.BooleanField(default=False)
    missing = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'{self.name}'

    def get_history(self):
        return Version.objects.get_for_object(self)
