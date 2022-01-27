from django import forms

from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['blog_title', 'text']
        labels = {'blog_title': 'Title of New Blog Post:',
                  'text': 'New Blog Text:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
