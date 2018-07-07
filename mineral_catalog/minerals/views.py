from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404


from .models import Mineral


def mineral_list(request):
    try:
        minerals = Mineral.objects.all()
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})

