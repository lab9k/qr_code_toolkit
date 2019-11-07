from django.db import models
from location_field.models.plain import PlainLocationField


class Job(models.Model):
    name = models.CharField(max_length=255)

    def get_qr_data(self):
        data = dict(id=self.id, name=self.name, type='Job')
        return data


class TrackedItem(models.Model):
    name = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['location'])
    is_in_use = models.BooleanField(default=False)
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, blank=True, null=True, related_name='current_items')

    def get_qr_data(self):
        data = dict(id=self.id, name=self.name, type='TrackedItem')
        return data
