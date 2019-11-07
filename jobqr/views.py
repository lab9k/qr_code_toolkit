import json
from django.views.generic import DetailView, ListView, View
from django.http import JsonResponse
from django.forms.models import model_to_dict

from jobqr.forms import QrForm
from jobqr.models import Job, TrackedItem


class JobListView(ListView):
    model = Job
    template_name = 'jobqr/job_list.html'


class JobView(View):
    def get(self, request, *args, **kwargs):
        view = JobDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = QrForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            url = data.get('scanned_url')

            job_id = kwargs.get('pk')
            job = Job.objects.get(pk=job_id)

            if url.endswith("/"):
                item_id = url[-2:-1]
            else:
                item_id = url[:-1]

            obj, created = TrackedItem.objects.get_or_create(pk=item_id)

            obj.job = job
            obj.is_in_use = True

            obj.save()

            current_items = [model_to_dict(x) for x in TrackedItem.objects.filter(job_id__exact=job_id)]

            return JsonResponse(
                {'item_id': item_id, 'job': model_to_dict(job), 'current_items': current_items})
        else:
            return JsonResponse({'err': 'form was not valid'})


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobqr/job_detail.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)

        full_url = self.request.build_absolute_uri()
        context['qr_url'] = full_url

        return context
