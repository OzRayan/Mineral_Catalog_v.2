from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404

from .models import Mineral


LABELS = [
    'category',
    'formula',
    'strunz_classification',
    'unit_cell',
    'color',
    'crystal_symmetry',
    'mohs_scale_hardness',
]

def mineral_list(request):
    try:
        minerals = Mineral.objects.all()
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = Mineral.objects.filter(id=pk).values()[0]
    print('******************')
    print(type(mineral))
    print('------------------')
    print(mineral)
    print('******************')
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral, 'labels': LABELS})
