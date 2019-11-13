import itertools

from django.db import models
from location_field.models.plain import PlainLocationField


class Job(models.Model):
    name = models.CharField(max_length=255)

    def items_str(self):
        items = [item.name for item in self.current_items.all()]
        return ", ".join(items)

    items_str.short_description = 'Currently tracked items'

    def __str__(self):
        return f'{self.name}'


class TrackedItem(models.Model):
    item_id = models.IntegerField(blank=False, primary_key=True, unique=True, auto_created=False)
    name = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['location'])
    is_in_use = models.BooleanField(default=False)
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, blank=True, null=True, related_name='current_items')

    def get_qr_data(self):
        data = dict(id=self.id, name=self.name, type='TrackedItem')
        return data

    def __str__(self):
        return f'{self.name}'
