import random
from django.db.models import CharField, Q
from django.shortcuts import render, Http404

from .models import Mineral


def mineral_detail(request, pk):
    """Mineral detail view
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


def mineral_by_alphabet(request, alpha):
    """Mineral by alphabet view
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


def mineral_by_group(request, group):
    """Mineral by group view
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


def mineral_by_color(request, color):
    """Mineral by color view
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
    """Mineral by crystal system view
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


def mineral_search(request):
    """Mineral search view
        request method GET, searches 'q' term in all fields using Q object
        more in RESOURCES.txt
    :return: - mineral_list.html + dictionary of mineral queries
    """
    term = request.GET.get('q')
    # # noinspection PyUnresolvedReferences
    # fields = [field for field in Mineral._meta.fields if isinstance(field, CharField)]
    # queries = [Q(**{field.name + '__icontains': term}) for field in fields]
    # query_set = Q()
    # for query in queries:
    #     query_set = query_set | query
    # # noinspection PyUnresolvedReferences
    # minerals = Mineral.objects.filter(query_set)

    minerals = Mineral.objects.filter(name__icontains=term)

    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def random_mineral(request):
    """Mineral random view, selects a random mineral
    :return: - mineral_detail.html + dictionary of random mineral values
    """
    # noinspection PyUnresolvedReferences
    minerals = Mineral.objects.all().values()
    mineral = random.choice(minerals)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})


def mineral_list(request):
    """Mineral list view, selects all the Mineral objects
    :return: - mineral_list.html + minerals Query
    """
    # noinspection PyUnresolvedReferences
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})
