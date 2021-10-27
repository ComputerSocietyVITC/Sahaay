from django.db import models
from .Issue_tags import TAG_CHOICES


class Issues(models.Model):
    Issue_Name = models.CharField(max_length=200, null=False, blank=False)
    Issue_Tags = models.CharField(max_length=255, null=False, choices=TAG_CHOICES)
    Issue_description = models.TextField()
    Issue_Images = models.ImageField()
    Issue_URL = models.URLField()
