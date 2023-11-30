from django.db import models

# Create your models here.
class property(models.Model):
    placename=models.CharField(max_length=40)
    location=models.CharField(max_length=40)
    image=models.ImageField(upload_to ='media/')
    acres=models.CharField(max_length=50)
    description=models.CharField(max_length=100)