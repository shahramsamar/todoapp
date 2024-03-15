from django.db import models


# Create your models here.
class BasicInformationModel(models.Model):
    about = models.TextField()
    age = models.PositiveIntegerField()
    email =models.EmailField()
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    language =models.CharField(max_length=255)
    
    class Meta:
        