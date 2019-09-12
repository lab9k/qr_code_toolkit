from django.db import models
from django.urls import reverse
from location_field.models.plain import PlainLocationField
from django.utils.timezone import now


class Work(models.Model):
    description = models.CharField(max_length=255, blank=False, null=False)
    start = models.DateTimeField(default=now, blank=False, null=False)
    end = models.DateTimeField(blank=True, null=True, editable=True, default=None)
    device = models.ForeignKey('Device', on_delete=models.CASCADE)

    def set_end(self):
        self.end = now()

    def __str__(self):
        return f'%s - %s' % (self.description, self.device)


class Device(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False, default='Ghent')
    location = PlainLocationField(based_fields=['location'])

    def get_absolute_url(self):
        return reverse("device_detail", kwargs={'id': self.pk})

    def __str__(self):
        return f'%s - %s - %s' % (self.name, self.location, self.city)
