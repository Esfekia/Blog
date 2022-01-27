from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def index(request):
    """The home page for the Blog."""
    return render(request, 'blogs/index.html')


def blogposts(request):
    """Show all blogposts."""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)
