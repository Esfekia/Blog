from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    """A blog for a user."""
    blog_title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a single representation of the model."""
        template = '{0.blog_title}'
        return template.format(self)
