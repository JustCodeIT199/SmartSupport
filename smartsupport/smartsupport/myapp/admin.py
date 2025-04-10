from django.contrib import admin
from myapp.models import UserProfile ,TaskDetail,MyCart
# Register your models here.

#UserProfile Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user','Address','RegistrationNo','Year','Department']

admin.site.register(UserProfile,UserProfileAdmin)


#TaskDetails Admin
class TaskDetailsAdmin(admin.ModelAdmin):
     list_display=['id','TASK_TITLE','TASK_CREATED','TASK_CLOSED','TASK_CREATED_ON','TASK_CLOSED_ON','TASK_DUE_DATE','TASK_DESCRIPTION','TASK_HOLDER','TASK_STATUS',]
admin.site.register(TaskDetail,TaskDetailsAdmin)

#MyCart Admin
class MyCartAdmin(admin.ModelAdmin):
     list_display=['id','user','task','task_count']
admin.site.register(MyCart,MyCartAdmin)