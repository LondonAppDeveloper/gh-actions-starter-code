from django.shortcuts import render


def index(request):
    """Render index page."""
    return render(request, 'home/index.html')
