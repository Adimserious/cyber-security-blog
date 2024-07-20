from django.db import models


CATEGORY_CHOICES = ((0, 'Cybersecurity attacks'), (1, "Cybersecurity domain"), (2, "Tipps and Guides"))
class CreateCategory(models.Model):
    """
    Create Category model
    """
    name = models.CharField(max_length=200)
    status = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    

    def __str__(self):
        return self.name
