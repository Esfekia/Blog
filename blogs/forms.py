from django import forms

from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['blog_title', 'text']
        labels = {'Blog Title': '', 'Blog Text': ''}
