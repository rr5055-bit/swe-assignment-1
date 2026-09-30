# Custom template filters for the CV templates
from django import template

register = template.Library()


@register.filter
def get_item(mapping, key):
    try:
        return mapping[key]
    except (KeyError, TypeError):
        return ""
