from django.shortcuts import render

# Create your views here.


def index(request):
    """The home page for the Blog."""
    return render(request, 'blogs/index.html')
