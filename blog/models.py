from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """
    Category model stores category for various blog posts.
    """
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

STATUS_CHOICES = ((0, 'pending'), (1, "done"))

class Blog_post(models.Model):
    """
    This model stores individual blog posts.
    """
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
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published"]

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('read_more', kwargs={'slug': self.slug})

    def __str__(self):
        return f"The title of this post is {self.title} | by {self.author}"

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    """
    This model stores comments on individual blog posts.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenters")
    post = models.ForeignKey(Blog_post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"Comment: {self.content}. by {self.author}"

class FeaturedPost(models.Model):
    """
    This model stores featured posts in slides.
    """
    post = models.OneToOneField(Blog_post, on_delete=models.CASCADE)
    featured_on = models.DateTimeField(auto_now_add=True)
    highlight_until = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    featured_image = models.ImageField(upload_to='featured_images/', null=True, blank=True)

    def __str__(self):
        return self.post.title



