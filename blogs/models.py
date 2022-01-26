from django.db import models

# Create your models here.


class BlogPost(models.Model):
    """A blog for a user."""
    blog_title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a single representation of the model."""
        template = '{0.blog_title} {0.text} '
        return template.format(self)
