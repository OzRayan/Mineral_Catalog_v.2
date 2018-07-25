from django import template

import minerals.models


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

# Displayed color options for mineral
COLORS = [
    'black',
    'blue',
    'brown',
    'green',
    'grey',
    'indigo',
    'orange',
    'pink',
    'purple',
    'red',
    'rose',
    'violet',
    'white',
    'yellow'
]

# Displayed crystal system options for mineral
SYSTEM = [
    'cubic',
    'hexagonal',
    'isometric',
    'monoclinic',
    'orthorhombic',
    'prismatic',
    'spheroidal',
    'tetragonal',
    'triclinic',
    'trigonal'
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


@register.inclusion_tag('minerals/color_list.html')
def color_list(cl):
    """Returns a dict of color list and 'cl' :param for color_list.html"""
    return {'colors': COLORS, 'cl': cl}


@register.inclusion_tag('minerals/crystal_list.html')
def crystal_list(cr):
    """Returns a dict of crystal system list and 'cr' :param for crystal_list.html"""
    return {'crystals': SYSTEM, 'cr': cr}


@register.inclusion_tag('minerals/group_list.html')
def group_list(gr):
    """Returns a dict of group list and 'gr' :param for group_list.html"""
    groups = minerals.models.Mineral.objects.values_list('group', flat=True).distinct()
    return {'groups': groups, 'gr': gr}

