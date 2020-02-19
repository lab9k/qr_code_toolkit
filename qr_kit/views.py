from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, FormView
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from qr_kit.models import QrCode, Category, QrCodeReport
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

    def get_context_data(self, **kwargs):
        context = super(QrCodeView, self).get_context_data(**kwargs)
        context['qr_url'] = self.request.build_absolute_uri()
        context['form'] = self.get_form()
        return context

    def get(self, request, *args, **kwargs):
        # noinspection PyAttributeOutsideInit
        self.object = self.get_object()
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        # noinspection PyAttributeOutsideInit
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            print('valid')
            return self.form_valid(form)
        else:
            print('invalid')
            return self.form_invalid(form)

    def get_form(self, form_class=None):
        obj = self.get_object()
        if self.request.method == 'POST':
            return DynamicQrForm(category=obj.category, data=self.request.POST)
        return DynamicQrForm(category=obj.category, filled_values=obj.values)

    def form_valid(self, form):
        # Save submitted form to database
        obj = self.get_object()

        pre_filled_values = obj.values
        form_values = form.cleaned_data
        form_values.update(pre_filled_values)

        report = QrCodeReport(values=form_values, qr_code=obj)
        report.save()

        # Redirect to category success_url
        return self.render_to_response(context=self.get_context_data())

    def form_invalid(self, form):
        return self.render_to_response(context=self.get_context_data())

    def get_success_url(self):
        return self.get_object().category.success_url
