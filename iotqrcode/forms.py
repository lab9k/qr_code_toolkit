from django.forms import ModelForm

from iotqrcode.models import Device


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'city', 'location']
