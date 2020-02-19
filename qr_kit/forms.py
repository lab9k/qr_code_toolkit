from django import forms
from qr_kit.models import Category


class DynamicQrForm(forms.Form):

    def __init__(self, category: Category = None, filled_values: dict = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('data') is not None:
            filled_values = kwargs.get('data')
        if category is not None and filled_values is not None:
            # get defined values from category. These values should be filled in in the form.
            defined_values = category.values_to_fill.all()

            # filled_values is either filled in from passed in data, or filled in from the qr_code object.
            values_to_fill = dict(
                [(value.parameter_name, filled_values.get(value.parameter_name, None))
                 for value in defined_values])

            # every value get's a field assigned to it, also the values that are filled already.
            # already filled values are set to readonly/disabled
            for field_name, field_value in values_to_fill.items():
                curr_value_obj = defined_values.get(parameter_name=field_name)
                if curr_value_obj.type == 'txt':
                    self.fields[field_name] = forms.CharField(label=curr_value_obj.name,
                                                              initial=field_value, required=False)
                    # set the readonly attribute to CharFields, as disabled textfields don't get posted in a html form
                    self.fields[field_name].widget.attrs['readonly'] = field_value is not None
                elif curr_value_obj.type == 'bool':
                    # as readonly only applies to the 'value' attribute in html, checkboxes won't disable properly like
                    # CharFields, because checkboxes apply the 'checked' html-attribute
                    self.fields[field_name] = forms.BooleanField(label=curr_value_obj.name,
                                                                 initial=field_value,
                                                                 required=False,
                                                                 disabled=field_value is not None)
