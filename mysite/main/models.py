from django.db import models

# Create your models here.

class TestImage(models.Model):
    name = models.CharField(max_length=100)
    imagelol = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name