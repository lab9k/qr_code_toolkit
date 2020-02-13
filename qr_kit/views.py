from django.views.generic import DetailView
from qr_kit.models import QrCode, Category
from qr_kit.forms import DynamicQrForm
from django.shortcuts import get_object_or_404


class QrCodeView(DetailView):
    template_name = 'qr_kit/qr_code.html'
    queryset = QrCode.objects.all()
    context_object_name = 'qr_code'

    def get_object(self, queryset=None) -> QrCode:
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(QrCode, uuid=uuid)

    def get(self, request, *args, **kwargs):
        # noinspection PyAttributeOutsideInit
        self.object = self.get_object()
        context = self.get_context_data()

        values_to_fill = self.object.category.values_to_fill.all()
        values_filled: dict = self.object.values
        context['values_filled'] = values_filled
        names = [x.name for x in values_to_fill]

        values_to_fill = dict([(name, values_filled.get(name, None)) for name in names])

        context['values_to_fill'] = values_to_fill

        form = DynamicQrForm(values_to_fill=values_to_fill)
        context['form'] = form

        return self.render_to_response(context)
