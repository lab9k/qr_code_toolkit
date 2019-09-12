from django.forms import ModelForm, CharField, HiddenInput

from iotqrcode.models import Device


class DeviceForm(ModelForm):
    job_desc = CharField(widget=HiddenInput())

    class Meta:
        model = Device
        fields = ['name', 'city', 'location']
