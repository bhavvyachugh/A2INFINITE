from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    

class Sheet(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Sheet/images", default="")
    
    def __str__(self):
        return self.name                      
