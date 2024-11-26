from django.shortcuts import render


def index(request):
    """Render index page."""
    # return None
    return render(request, 'home/index.html')
