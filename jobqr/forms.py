from django import forms
from rest_framework.exceptions import ValidationError

from jobqr.models import TrackedItem


class QrForm(forms.Form):
    item_id = forms.IntegerField()
    location = forms.CharField(max_length=128)

    def clean_item_id(self):
        item_id = self.cleaned_data['item_id']
        if not TrackedItem.objects.filter(item_id=item_id).exists():
            raise ValidationError(detail="Item does not exist. Have you tried registering it?")
        else:
            return item_id


class RegisterForm(forms.Form):
    item_name = forms.CharField(max_length=255)
    item_url = forms.URLField()
