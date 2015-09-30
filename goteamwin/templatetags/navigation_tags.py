from django import template
from series.models import Series

register = template.Library()

@register.assignment_tag
def series_list():
    return Series.objects.all()