from django.db import models

# Create your models here.
class Note(models.Model):
    content = models.CharField((""), max_length=100)
    done = models.BooleanField()
