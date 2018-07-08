from django import template

register = template.Library()


@register.filter
def clean_title(title):
    return title.replace('_', ' ')
