from django.contrib import admin
from django.urls import path, include
from myapp import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('base/',views.Basepage,name="base"),
   path('login/',views.LoginView,name="login"),
   path('logout/',views.LogoutView,name="logout"),
   path('register/',views.RegisterView,name="register"),

   path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
   path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
   path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
   path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
   path('ChangePassword/', views.Change_Password,name='ChangePassword'),
   path('profile/', views.User_Profile,name='profile'),
   path('update_profile/<int:pk>', views.update_profile,name='update_profile'),
   path('taskdetails/', views.TaskDetails,name='taskdetails'), 
   path('taskinfo/<int:pk>', views.TaskInfo,name='taskinfo'), 
   path('updatetask/<int:pk>', views.updatetask,name='updatetask'),
   path('deletetask/<int:pk>', views.deletetask,name='deletetask'),
   path('accepttask/<int:pk>', views.accepttask,name='accepttask'),
   path('mycart', views.MyCarts,name='mycart'),
   path('removetask/<int:pk>', views.RemoveTask,name='removetask'),
   path('closedtask/<int:pk>', views.ClosedTask,name='closedtask'),
   path('reopentask/<int:pk>', views.reopentask,name='reopentask'),
   path('resolvedtask/<int:pk>', views.resolvedtask,name='resolvedtask'),
   path('assign_task/<int:pk>/', views.assign_task, name='assign_task'),
   path('status_pie', views.dashboard_pie,name='status_pie'),
   path('status_task', views.pie_chart,name='status_task'),
   path('status_bar', views.Bar_chart,name='status_bar'),




   
  

   
]
