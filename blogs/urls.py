"""Defines URL patterns for blogs."""

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows the blog entries.
    path('blogposts/', views.blogposts, name='blogposts'),
    # Detail page for an individual blog post.
    path('blogposts/<int:blogpost_id>/', views.blogpost, name='blogpost'),

]
