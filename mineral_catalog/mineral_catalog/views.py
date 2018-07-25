from django.shortcuts import Http404, render

import minerals.models


def index(request):
    """Home page view - filters name field by letter 'A'
    :parameter: - request
    :return - index.html, minerals dict startswith 'A'
    """
    try:
        minerals_set = minerals.models.Mineral.objects.filter(name__startswith="A")
    except minerals.models.Mineral.DoesNotExist:
        raise Http404
    return render(request, 'index.html', {'minerals': minerals_set})

