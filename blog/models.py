from django.conf import settings
from django.db import models

from core.models import UserProfile

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    summary = models.TextField()
    post = models.TextField()
    image = models.ImageField()
    publication_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    last_accessed = models.DateTimeField()

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

