from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from iotqrcode.models import Device, Work
from iotqrcode.forms import DeviceForm


class DeviceListView(ListView):
    template_name = 'iotqrcode/device_list.html'
    model = Device
    queryset = Device.objects.all()
    context_object_name = 'devices'


class DeviceView(FormView):
    template_name = 'iotqrcode/device_detail.html'
    form_class = DeviceForm

    def get_initial(self):
        initial = super(DeviceView, self).get_initial()
        device = Device.objects.get(pk=self.kwargs.get("id"))
        initial.update({'name': device.name, 'location': device.location, 'city': device.city})
        return initial

    def get_context_data(self, **kwargs):
        context = super(DeviceView, self).get_context_data(**kwargs)
        device = Device.objects.get(pk=self.kwargs.get('id'))
        context['device'] = device
        context['is_worked_on'] = Work.objects.filter(device_id__exact=device.pk).latest('start').end is None
        return context

    def form_valid(self, form):
        device = Device.objects.get(pk=self.kwargs.get('id'))
        print(form.cleaned_data)
        if 'update_device' in self.request.POST:
            device.location = form.cleaned_data.get("location")
            device.name = form.cleaned_data.get("name")
            device.city = form.cleaned_data.get("city")
            device.save()
        if 'start_work' in self.request.POST:
            job = Work(description=form.cleaned_data.get('job_desc'), device=device)
            job.save()
        if 'end_work' in self.request.POST:
            job = Work.objects.filter(device_id__exact=device.pk).latest('start')
            job.set_end()
            job.save()
        return self.render_to_response(self.get_context_data(form=form))


class DeviceQRView(TemplateView):
    template_name = 'iotqrcode/device_qr.html'

    def get_context_data(self, **kwargs):
        context = super(DeviceQRView, self).get_context_data(**kwargs)
        full_url = self.request.build_absolute_uri("/")

        url = full_url + "device/" + str(self.kwargs.get("id")) + "/"
        context["qr_data"] = url
        context["device"] = Device.objects.get(pk=self.kwargs.get('id'))
        return context


class DeviceQRListView(ListView):
    template_name = 'iotqrcode/device_qr_list.html'
    model = Device
    queryset = Device.objects.all()
    context_object_name = 'devices'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeviceQRListView, self).get_context_data(**kwargs)
        full_url = self.request.build_absolute_uri("/")

        devices = Device.objects.all()
        devices_urls = [{'url': full_url + "device/" + str(d.pk) + "/", 'device': d} for d in devices]
        context["devices"] = devices_urls

        return context
