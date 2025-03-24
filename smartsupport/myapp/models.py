from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#UserProfile Model
class UserProfile(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Address=models.CharField(max_length=100)
    RegistrationNo=models.CharField(max_length=100,default='0000CE00F')
    Year=models.CharField(max_length=100, default='First Year')
    Department=models.CharField(max_length=100,default='Engineering')
