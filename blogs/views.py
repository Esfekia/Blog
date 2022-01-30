from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm


def index(request):
    """The home page for the Blog."""
    return render(request, 'blogs/index.html')


def blogposts(request):
    """Show all blogposts."""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/blogposts.html', context)


def blogpost(request, blogpost_id):
    """Show a single blogpost."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    context = {'blogpost': blogpost}
    return render(request, 'blogs/blogpost.html', context)


@login_required
def new_blogpost(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('blogs:blogposts')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blogpost.html', context)


@login_required
def edit_blogpost(request, blogpost_id):
    """Edit an existing blogpost."""
    blogpost = BlogPost.objects.get(id=blogpost_id)
    if blogpost.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current blogpost.
        form = BlogPostForm(instance=blogpost)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogpost', blogpost_id=blogpost.id)

    context = {'blogpost': blogpost, 'form': form}
    return render(request, 'blogs/edit_blogpost.html', context)
