from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#UserProfile Model
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Address=models.CharField(max_length=100)
    RegistratioNo=models.CharField(max_length=100,default='0000CE000')
    Year=models.CharField(max_length=100, default='First Year')
    Department=models.CharField(max_length=100,default='Engineering')
