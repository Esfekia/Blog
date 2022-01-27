"""Defines URL patterns for blogs."""

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows the blog entries.
    path('blogposts/', views.blogposts, name='blogposts'),
]
