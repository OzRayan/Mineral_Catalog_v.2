import random
import re
from django.shortcuts import render
from django.http import Http404

from .models import LABELS, Mineral


def mineral_detail(request, pk):
    mineral = Mineral.objects.filter(id=pk).values()[0]
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral, 'labels': LABELS})


def random_mineral(request):
    minerals = Mineral.objects.all().values()
    mineral = random.choice(minerals)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral, 'labels': LABELS})


def mineral_list(request):
    try:
        minerals = Mineral.objects.all()
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})
