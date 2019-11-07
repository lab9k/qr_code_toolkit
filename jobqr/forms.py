from django import forms


class QrForm(forms.Form):
    scanned_url = forms.URLField()


class RegisterForm(forms.Form):
    item_name = forms.CharField(max_length=255)
    item_url = forms.URLField()
