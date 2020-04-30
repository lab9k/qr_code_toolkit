from django.db import models
from django.utils.timezone import now

from location_field.models.plain import PlainLocationField
from reversion.models import Version


class Job(models.Model):
    name = models.CharField(max_length=255)

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
