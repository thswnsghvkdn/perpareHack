from django.db import models

# Create your models here.

class Notice(models.Model) :
    images = models.ImageField(null = True , blank = True, upload_to = "images")
    title = models.CharField(null=True , max_length=500)
    body = models.CharField(null = True, max_length=500)
    userName = models.CharField(null = True, max_length=500)