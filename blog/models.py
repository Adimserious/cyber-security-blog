from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name


STATUS_CHOICES = ((0, 'pending'), (1, "done"))

# Create your models here.
class Blog_post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    image = CloudinaryField("image", default='placeholder')
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    body_content = models.TextField()
    snippet = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="blog_post", default=1)
    likes = models.ManyToManyField(User, related_name="post_likes")
    # Meta data class with ordering attribute to sort result by the published field
    class Meta:
        ordering = ["-published"]

    def  total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f"The title of this post is {self.title} | by {self.author}"



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenters")
    post = models.ForeignKey(Blog_post, on_delete=models.CASCADE, related_name="comments") 
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"Comment: {self.content}. by {self.author}"         
