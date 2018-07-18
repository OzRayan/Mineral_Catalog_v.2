from django.shortcuts import render,Http404
from minerals.models import Mineral


def index(request):
    """Home page view
    :parameter: - request
    :return - index.html, minerals dict startswith 'A'
    """
    try:
        minerals = Mineral.objects.filter(name__startswith="A")
    except Mineral.DoesNotExist:
        raise Http404
    return render(request, 'index.html', {'minerals': minerals})

