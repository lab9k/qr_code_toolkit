from django import forms


class DynamicQrForm(forms.Form):

    def __init__(self, values_to_fill: dict = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if values_to_fill is not None:
            for field_name, field_value in values_to_fill.items():
                print(field_name, field_value)
                self.fields[field_name] = forms.CharField(label=field_name, initial=field_value,
                                                          )
                self.fields[field_name].widget.attrs['readonly'] = field_value is not None
