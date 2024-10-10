import re
from django import template
from django.utils.text import slugify

register = template.Library()

@register.filter(name='custom_slugify')
def custom_slugify(value):
    # Replace double quotes with a custom string
    value = value.replace('"', 'inch').replace("-", "_").replace(",", "/")
    # Then slugify the name
    return slugify(value)
