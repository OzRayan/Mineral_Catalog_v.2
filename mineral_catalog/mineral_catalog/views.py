from django.shortcuts import render


def index(request):
    """Home page view
    :parameter: - request
    :return - index.html
    """
    return render(request, 'index.html')