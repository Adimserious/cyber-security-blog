from django.db import models

class CreateCategory(models.Model):
    """
    Create Category model
    """
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
