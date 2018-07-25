import random

from django.db.models import Q    # , CharField  ### for mineral_search()
from django.shortcuts import Http404, render

from .models import Mineral


def mineral_by_alphabet(request, alpha):
    """Mineral by alphabet view - filters name filed by first letter
    :input: - alpha - mineral which starts with the letter alpha
    :return: - mineral_list.html + dictionary of mineral startswith alpha
    """
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(name__startswith=alpha)
    # noinspection PyUnresolvedReferences
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals, 'alpha': alpha})


def mineral_by_color(request, color):
    """Mineral by color view - filters color field by 'color'
    :input: - color - color name
    :return: - mineral_list.html + dictionary of mineral objects
    """
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(color__icontains=color)
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals, 'cl': color})


def mineral_by_crystal_system(request, crystal):
    """Mineral by crystal system view - filters crystal system field by
                crystal system
    :input: - crystal - crystal system name
    :return: - mineral_list.html + dictionary of mineral objects
    """
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(crystal_system__icontains=crystal)
    except Mineral.DoesNotExist:
        raise Http404

    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals, 'cr': crystal})


def mineral_detail(request, pk):
    """Mineral detail view - filters id field by 'pk'
    :input: - pk - mineral id
    :return: - mineral_detail.html + dictionary of mineral values
    """
    # noinspection PyUnresolvedReferences
    try:
        mineral = Mineral.objects.filter(id=pk).values()[0]
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})


def mineral_by_group(request, group):
    """Mineral by group view - filters group field by 'group'
    :input: - group - group name
    :return: - mineral_list.html + dictionary of mineral objects
    """
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(group=group)
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals, 'gr': group})


def mineral_list(request):
    """Mineral list view, selects all the Mineral objects
    :return: - mineral_list.html + minerals Query
    """
    # noinspection PyUnresolvedReferences
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_search(request):
    """Mineral search view - selects one field or multiple fields from which
                            filters the 'q' value
        request method GET, targets <input> element name attribute from layout.html
                            with value of 'q'
                            targets <select> element name attribute from layout.html
                            with value of 'mySelect'
        more in RESOURCES.txt
    :return: - mineral_list.html + dictionary of mineral queries
    """
    term = request.GET.get('q')
    field = request.GET.get('mySelect')

    # Unwanted fields list
    no_field = ['id', 'image_filename', 'image_caption']

    # If fd is not 'all' then it choose the fd value as field name
    if field != 'all':
        fields = [Mineral._meta.get_field(field)]
    else:
        # 'isinstance(field, CharField)' for selected Model type!

        # Else it choose from all fields except no_field items
        fields = [fd for fd in Mineral._meta.get_fields() if fd.name not in no_field]
    queries = [Q(**{fd.name + '__icontains': term}) for fd in fields]
    query_set = Q()
    for query in queries:
        query_set = query_set | query

    # noinspection PyUnresolvedReferences
    minerals = Mineral.objects.filter(query_set)

    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def random_mineral(request):
    """Mineral random view, selects a random mineral
    :return: - mineral_detail.html + dictionary of random mineral values
    """
    # noinspection PyUnresolvedReferences
    minerals = Mineral.objects.all().values()
    mineral = random.choice(minerals)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})
