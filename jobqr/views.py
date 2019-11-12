from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.generic import DetailView, ListView, View, RedirectView, TemplateView

from jobqr.forms import QrForm, RegisterForm
from jobqr.models import Job, TrackedItem


class JobListView(ListView):
    model = Job
    template_name = 'jobqr/job_list.html'


class JobView(View):
    def get(self, request, *args, **kwargs):
        view = JobDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = QrForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            item_id = data.get('item_id')

            job_id = kwargs.get('pk')
            job = Job.objects.get(pk=job_id)

            obj = TrackedItem.objects.get(item_id=item_id)

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


class HomeView(RedirectView):
    pattern_name = 'job_list'
    query_string = True
    permanent = True


class RegisterView(TemplateView):
    http_method_names = ['get', 'post']
    template_name = 'jobqr/register.html'

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['item_name']
            item_url = form.cleaned_data['item_url']
            item_id = int(item_url[-3:].replace('/', ''))
            found_item = TrackedItem.objects.filter(item_id=item_id)
            if found_item.count() > 0:
                return self.render_to_response(context={'message': 'That url is already registered', 'success': False})
            else:
                new_item = TrackedItem.objects.create(name=item_name, item_id=item_id)
                new_item.save()
                return self.render_to_response(context={'message': 'Item added successfully', 'success': True})
        return self.render_to_response(context={'message': 'Form invalid', 'success': False})
