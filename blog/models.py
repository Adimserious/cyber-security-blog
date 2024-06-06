from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class blog_posts(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    body_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    # Meta data class with ordering attribute to sort result by the published field
    class Meta:
        ordering = ["-published"]
    