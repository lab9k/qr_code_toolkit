from django.shortcuts import render
from django.http.response import HttpResponseNotAllowed
from jobqr.models import TrackedItem


def register_item(request):
    if request.method == 'GET':
        return render(request, template_name='register/index.html', context={})
    elif request.method == 'POST':
        return render(request, template_name='register/index.html', context={})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
