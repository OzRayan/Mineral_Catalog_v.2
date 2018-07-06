from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404


from .models import Mineral


def minerals_list(request):
    try:
        minerals = get_object_or_404(Mineral.objects.all())
    except Mineral.DoesNotExist:
        raise Http404("Fail")
    return render(request, 'mineral/mineral_list.html', {'minerals': minerals})

