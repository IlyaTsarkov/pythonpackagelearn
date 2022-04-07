from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Package(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





