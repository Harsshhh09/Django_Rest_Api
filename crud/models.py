from django.db import models

# Create your models here.
class Anime(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

