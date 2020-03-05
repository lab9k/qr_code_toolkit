from urllib.parse import urlencode

from django.shortcuts import redirect

HTTP_METHOD_CHOICES = [
    ('GET', 'GET'),
    ('POST', 'POST'),
    ('PUT', 'PUT'),
    ('DELETE', 'DELETE'),
]

VALUE_TYPE_CHOICES = [
    ('txt', 'Text'),
    ('bool', 'Boolean'),
]


def redirect_params(url, params=None):
    response = redirect(url, permanent=False)
    if params:
        query_string = urlencode(params)
        response['Location'] += f'?{query_string}'
    return response
