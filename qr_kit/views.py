from django.views.generic import DetailView, FormView
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from qr_kit.models import QrCode, Category
from qr_kit.forms import DynamicQrForm


class QrCodeView(DetailView, FormMixin):
    template_name = 'qr_kit/qr_code.html'
    queryset = QrCode.objects.all()
    context_object_name = 'qr_code'
    success_url = ''
    form_class = DynamicQrForm

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

    def post(self, request, *args, **kwargs):
        # noinspection PyAttributeOutsideInit
        self.object = self.get_object()
        values_to_fill = self.object.category.values_to_fill.all()
        names = [x.name for x in values_to_fill]
        print(request.POST)
        values_to_fill = dict([(name, request.POST.get(name, None)) for name in names])
        form = DynamicQrForm(values_to_fill=values_to_fill, data=request.POST)
        if form.is_valid():
            print('valid')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return self.render_to_response(context={'form': form})

    def form_invalid(self, form):
        return self.render_to_response(context={'form': form})

    def get_success_url(self):
        return self.get_object().category.success_url
