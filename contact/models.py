from django.db import models

# Create your models here.
class RequestContact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Request Contact from {self.name}"
