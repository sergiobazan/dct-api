from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    releaseYear = models.IntegerField()
    description = models.CharField(max_length=255)
    images = models.JSONField()
