from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#UserProfile Model
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Address=models.CharField(max_length=100)
    RegistrationNo=models.CharField(max_length=100,default='0000CE00F')
    Year=models.CharField(max_length=100, default='First Year')
    Department=models.CharField(max_length=100,default='Engineering')


#TaskDetails Model
class TaskDetail(models.Model):
    TASK_TITLE=models.CharField(max_length=100)
    TASK_CREATED=models.ForeignKey(User,related_name='CREATED_BY',on_delete=models.CASCADE,null=True)
    TASK_CLOSED=models.ForeignKey(User,related_name='CLOSED_BY',on_delete=models.CASCADE,null=True)
    TASK_CREATED_ON=models.DateField(auto_now_add=True,null=True)
    TASK_CLOSED_ON=models.DateField(null=True)
    TASK_DUE_DATE=models.DateField()
    #TASK_ASSIGNED_TO=models.IntegerField()
    TASK_DESCRIPTION=models.CharField(max_length=300)
    choice=[('Open','Open'),('Inprocess','Inprocess'),('Closed','Closed'),('Reopen','Reopen'),('Expired','Expired'),('Resolved','Resolved')]
    TASK_STATUS=models.CharField(max_length=100,choices=choice,default='Open')   
    TASK_HOLDER=models.CharField(max_length=100,null=True) 
    profile_image= models.ImageField(null=True,blank=True,upload_to="image/")
 



#MyCart Model
class MyCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.ForeignKey(TaskDetail,related_name='tasks',on_delete=models.CASCADE)
    task_count=models.IntegerField(default=1)    