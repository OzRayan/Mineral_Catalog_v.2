import random
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
        minerals = Mineral.objects.filter(name__startswith=alpha)
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals, 'alpha': alpha, 'alphabet': ALPHABET})


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
