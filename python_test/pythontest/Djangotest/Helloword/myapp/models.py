from django.db import models

# Create your models here.
class person(models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)