from django.db import models

class Messages(models.Model):
    username = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)