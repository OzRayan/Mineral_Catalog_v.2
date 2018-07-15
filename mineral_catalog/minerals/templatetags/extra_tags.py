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


@register.inclusion_tag('minerals/mineral_groups.html')
def mineral_group_list(current_group=None):
    """Returns dict of mineral groups to display in filter"""
    groups = (Mineral.objects.values_list('group', flat=True)
                             .distinct())
    groups = list(groups)
    groups.sort()
    return {'groups': groups, 'current_group': current_group}