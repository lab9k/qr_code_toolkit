from django.views.generic import RedirectView


class HomeView(RedirectView):
    pattern_name = 'job_list'
    query_string = True
    permanent = True
