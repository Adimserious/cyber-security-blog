from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class About_page(models.Model):
    title = models.CharField(max_length=200)
    body_content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"The title of this post is {self.title}"    
