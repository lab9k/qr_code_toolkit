from django import forms


class DynamicQrForm(forms.Form):

    def __init__(self, values_to_fill: dict = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field_value in values_to_fill.items():
            print(field_name, field_value)
            self.fields[field_name] = forms.CharField(label=field_name, initial=field_value,
                                                      disabled=field_value is not None)
