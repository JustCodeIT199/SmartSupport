from django.contrib import admin
from django.urls import path, include
from myapp import views 
urlpatterns = [
   path('base/',views.Basepage,name="base"),
   path('login/',views.LoginView ,name="login"),
   
]
