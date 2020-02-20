from django import template
from django.core.serializers import serialize
import json

from django.db.models import QuerySet
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
def jsonify(obj):
    if isinstance(obj, QuerySet):
        return serialize('json', obj)
    return json.dumps(obj)
