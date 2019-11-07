from django import forms


class QrForm(forms.Form):
    scanned_url = forms.URLField()
