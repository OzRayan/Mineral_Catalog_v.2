from django import template

register = template.Library()


@register.filter
def get_item(key):
    return [key]


@register.filter
def clean_title(title):
    return title.replace('_', ' ')
