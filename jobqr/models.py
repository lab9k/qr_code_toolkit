from django.db import models
from location_field.models.plain import PlainLocationField
from reversion.models import Version


class Job(models.Model):
    name = models.CharField(max_length=255)

    def items_str(self):
        items = [item.name for item in self.current_items.all()]
        return ", ".join(items)

    items_str.short_description = 'Currently tracked items'

    def __str__(self):
        return f'{self.name}'


class JobImage(models.Model):
    image = models.ImageField(upload_to='jobs/', blank=True, default=None)
    job = models.ForeignKey(to=Job, on_delete=models.CASCADE, related_name='images')


class TrackedItem(models.Model):
    item_id = models.IntegerField(blank=False, primary_key=True, unique=True, auto_created=False)
    name = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['location'])
    is_in_use = models.BooleanField(default=False)
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, blank=True, null=True, related_name='current_items')
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    missing = models.BooleanField(default=False)

    def get_qr_data(self):
        data = dict(id=self.id, name=self.name, type='TrackedItem')
        return data

    def get_history(self):
        obj = Version.objects.get_for_object(self)
        return obj

    def __str__(self):
        return f'{self.name}'


class MethodTemplate(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    methods = models.ManyToManyField(to='Method', related_name='template', related_query_name='template')


class Method(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
