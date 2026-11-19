from django.db import models

# Create your models here.

class Form(models.Model):
     username = models.CharField(max_length=30)
     subject = models.CharField(max_length=20)
     age = models.IntegerField(null=True, blank=True)