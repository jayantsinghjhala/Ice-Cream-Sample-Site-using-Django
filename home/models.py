from django.db import models

# Create your models here.
class Contact(models.Model):
     name=models.CharField(max_length=50)
     email=models.CharField(max_length=122)
     phone=models.CharField(max_length=10)
     desc=models.TextField()
     create_date=models.DateField()
     def __str__(self):
        return "Name:"+self.name+" | Email:"+self.email+" | Phone:"+self.phone
