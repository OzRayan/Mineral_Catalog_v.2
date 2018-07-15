import random
from django.db.models import CharField, Q
from django.shortcuts import render, Http404

from .models import Mineral

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ'


def mineral_detail(request, pk):
    """Mineral detail view, selects a Mineral by id
    :return: - mineral_detail.html + dictionary of mineral values
    """
    # noinspection PyUnresolvedReferences
    mineral = Mineral.objects.filter(id=pk).values()[0]
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})


def mineral_by_alphabet(request, alpha):
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(name__startswith=alpha)
    # noinspection PyUnresolvedReferences
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals, 'alpha': alpha, 'alphabet': ALPHABET})


def mineral_by_group(request, group):
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(group=group)
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_by_color(request, color):
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(color=color)
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_by_crystal_habit(request, crystal_habit):
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(crystal_habit=crystal_habit)
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_by_crystal_system(request, crystal_system):
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(crystal_system=crystal_system)
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_by_optical_properties(request, optical_properties):
    try:
        # noinspection PyUnresolvedReferences
        minerals = Mineral.objects.filter(optical_properties=optical_properties)
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_search(request):
    term = request.GET.get('q')
    # noinspection PyUnresolvedReferences
    fields = [field for field in Mineral._meta.fields if isinstance(field, CharField)]
    queries = [Q(**{field.name + '__icontains': term}) for field in fields]
    query_set = Q()
    for query in queries:
        query_set = query_set | query
    # noinspection PyUnresolvedReferences
    minerals = Mineral.objects.filter(query_set)
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_by_a(request):
    try:
        minerals = Mineral.objects.filter(name__startswith="A")
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def random_mineral(request):
    """Mineral random view, selects a random mineral
    :return: - mineeral_detail.html + dictionary of random mineral values
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
