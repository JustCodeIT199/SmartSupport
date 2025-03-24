from django.contrib import admin
from myapp.models import UserProfile
# Register your models here.

#UserProfile Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['User','Address','RegistrationNo','Year','Department']

admin.site.register(UserProfile,UserProfileAdmin)
