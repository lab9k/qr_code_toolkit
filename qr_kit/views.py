from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin
from rest_framework.views import APIView

from qr_kit.models import QrCode, QrCodeReport
from qr_kit.forms import DynamicQrForm
from qr_kit.util import redirect_params


class QrCodeView(DetailView, FormMixin):
    template_name = 'qr_kit/qr_code.html'
    queryset = QrCode.objects.all()
    context_object_name = 'qr_code'
    success_url = ''
    form_class = DynamicQrForm

    def get(self, request, *args, **kwargs):
        """
        get the qr detail page. This view redirects to an external form, or builds a form with the values defined in
        it's category combined with the default values from the qr_code.
        """
        # noinspection PyAttributeOutsideInit
        self.object = self.get_object()
        if self.object.category.redirect_to_form_with_query_params:
            # redirect to form, with query params filled in
            return redirect_params(url=self.object.category.endpoint, params={
                **self.object.values,
                'next': self.object.category.success_url
            })
        else:
            return super(QrCodeView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        POST handler for this QrCode object form, will validate the form and handle accordingly.
        """
        # noinspection PyAttributeOutsideInit
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_object(self, queryset=None) -> QrCode:
        """
        :return: the QrCode object this view points to. (according to uuid slug in the resolved url)
        """
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(QrCode, uuid=uuid)

    def get_form(self, form_class=None):
        """
        Returns a form based on the passed in values
        """
        obj = self.get_object()
        if self.request.method == 'POST':
            return DynamicQrForm(category=obj.category, data=self.request.POST)
        return DynamicQrForm(category=obj.category, filled_values=obj.values)

    def form_valid(self, form):
        """
        Handles a valid form, redirects to the QrCode.Category.success_url url
        """
        # Save submitted form to database
        obj = self.get_object()

        pre_filled_values = obj.values
        form_values = form.cleaned_data
        # make sure pre_filled_values from qr_code are not tampered with
        form_values.update(pre_filled_values)

        report = QrCodeReport(values=form_values, qr_code=obj)
        report.save()

        # Redirect to category success_url
        return self.render_to_response(context=self.get_context_data())

    def form_invalid(self, form):
        """
        Handles an invalid form.
        """
        return self.render_to_response(context=self.get_context_data())

    def get_success_url(self):
        """
        :returns success_url for the current QrCode object
        """
        return self.get_object().category.success_url


class ReportView(ListView, UserPassesTestMixin):
    queryset = QrCodeReport.objects.all()
    template_name = 'qr_kit/report.html'
    context_object_name = 'reports'

    def test_func(self):
        # Check if user is logged in as a superuser
        return self.request.user.is_superuser
