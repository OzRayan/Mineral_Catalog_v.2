from django import template

from minerals.models import Mineral


register = template.Library()


# Displayed fields for mineral
LABELS = [
    'category',
    'formula',
    'strunz_classification',
    'unit_cell',
    'color',
    'crystal_symmetry',
    'mohs_scale_hardness',
    'group',
    'optical_properties',
    'crystal_habit',
    'specific_gravity',
    'crystal_system',
    'luster',
]


# Remove _ from field name
@register.filter
def clean_title(title):
    return title.replace('_', ' ')


# Checks if field is in LABELS list
@register.filter
def check(field):
    if field in LABELS:
        return True


@register.simple_tag
def filters():
    return FILTERS


@register.inclusion_tag('minerals/group_list.html')
def group_list(gr):
    """Returns dict of mineral groups to display in filter"""
    groups = Mineral.objects.values_list('group', flat=True).distinct()
    return {'groups': groups, 'gr': gr}

