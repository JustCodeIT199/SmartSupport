from django.shortcuts import redirect, render
from myapp.forms import LoginForm,RegisterForm,UserProfileForm,TaskDetailForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from myapp.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from myapp.models import TaskDetail,MyCart
from django.utils import timezone
import seaborn as sns



# Create your views here.
def Basepage(request):
    if request.user.is_authenticated:
        Taskdatas=TaskDetail.objects.all()
        return render(request,'Base.html',{'Taskdatas':Taskdatas})
    else:
       messages.success(request,"You must have to login to see Task!")
       return redirect('login')  
     
#Login View
def LoginView(request):
    if request.method =='POST':
        forms =LoginForm(request.POST)
        if forms.is_valid():
            username=forms.cleaned_data['username']
            password=forms.cleaned_data['password']
            user=authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"✅ Login Successful! Welcome back!")
                #return render(request,'Base.html')
                return redirect('base')
            else:
                messages.error(request,"Username or Password not Valid")
                return render(request,'Login.html',{'forms':forms})
    else:
        forms =LoginForm()
        return render(request,'Login.html',{'forms':forms})
    
#LogoutView
def LogoutView(request):
    logout(request)
    messages.error(request,"⚠️ You have been successfully logged out. See you again soon!")
    return redirect('login')

#Register
from django.contrib.auth.models import User

# Register
def RegisterView(request):
    if request.method == 'POST':
        Register_forms = RegisterForm(request.POST)
        UserProfile_forms = UserProfileForm(request.POST)
        if Register_forms.is_valid() and UserProfile_forms.is_valid():
            user = Register_forms.save()
            UserProfileforms = UserProfile_forms.save(commit=False)
            UserProfileforms.User = user
            UserProfileforms.Address = UserProfile_forms.cleaned_data['Address']
            UserProfileforms.RegistrationNo = UserProfile_forms.cleaned_data['RegistrationNo']
            UserProfileforms.Year = UserProfile_forms.cleaned_data['Year']
            UserProfileforms.Department = UserProfile_forms.cleaned_data['Department']
            UserProfileforms.save()
            messages.success(request, "✅ You have been Registered Successfully!")
            return redirect('login')
        else:
            messages.error(request, "⚠️ You have not entered correct data!")
            return redirect('register')
    else:
        Register_forms = RegisterForm()
        UserProfile_forms = UserProfileForm()

        return render(request, 'Register.html', {'Register_forms': Register_forms, 'UserProfile_forms': UserProfile_forms})
    


    #Change_Password
def Change_Password(request):
    if request.method=='POST':
     fm=PasswordChangeForm(user=request.user,data=request.POST)  
     if fm.is_valid():
          fm.save()
          update_session_auth_hash(request,fm.user)
          messages.success(request,'Your password has be changed succesfully.....') 
          return redirect('base')  
    else:
       fm=PasswordChangeForm(user=request.user)
    return render (request,'Change_Password.html',{'fm':fm})


# #User_Profile
# def User_Profile(request):
#     if request.user.is_authenticated:
#         user=request.user
#         ProfileDatas=UserProfile.objects.filter(user=user)
#        # AccountDatas=Account.objects.filter(ACCOUNT_HOLDER=user)
#         return render(request,'Userprofile.html',{'ProfileDatas':ProfileDatas})
#     else:
#        messages.success(request,"You must have to login to see profile!")
#        return redirect('login') 

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserProfile

def User_Profile(request):
    if request.user.is_authenticated:
        user = request.user
        ProfileDatas = UserProfile.objects.filter(user=user)
        # If you need account data as well, uncomment and adjust accordingly:
        # AccountDatas = Account.objects.filter(ACCOUNT_HOLDER=user)
        return render(request, 'Userprofile.html', {'ProfileDatas': ProfileDatas})
    else:
        messages.error(request, "You must log in to see your profile!")
        return redirect('login')


#Update_Profile
def update_profile(request,pk):
    if request.user.is_authenticated:
        ProfileDatas=UserProfile.objects.get(id=pk)
        form=UserProfileForm(request.POST or None,instance=ProfileDatas)
        if form.is_valid():
            form.save()
            messages.success(request,"profile Updated succesfully.....")
            return redirect('profile') 
        return render(request,'Update_Profile.html',{'form':form})    
    else:
       messages.success(request,"You must have to login to update profile!")
       return redirect('login')    



# #Task Creation Function
# def TaskDetails(request):
#     if request.user.is_authenticated:
#         if request.method=='POST':
#             form=TaskDetailForm(request.POST)
#             if form.is_valid():
#                 Task=form.save(commit=False) 
#                 Task.TASK_CREATED=request.user
#                 Task.save()
#                 messages.success(request,"Task Created Succesfully.....")
#             return redirect('base')
#         else:
#             form=TaskDetailForm()
#             return render(request,'TaskDetail.html',{'form':form}) 
#     else:
#        messages.success(request,"You must have to login to Create Task!")
#        return redirect('login')     

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TaskDetailForm

def TaskDetails(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskDetailForm(request.POST, request.FILES)  # Include request.FILES here
            if form.is_valid():
                Task = form.save(commit=False)
                Task.TASK_CREATED = request.user
                Task.save()
                messages.success(request, "Task Created Successfully.....")
                return redirect('base')
        else:
            form = TaskDetailForm()

        return render(request, 'TaskDetail.html', {'form': form})
    else:
        messages.error(request, "You must log in to create a task!")
        return redirect('login')


#Task Information
def TaskInfo(request,pk):
    if request.user.is_authenticated:
        taskinfos=TaskDetail.objects.get(id=pk)
        # Comments= UserComments.objects.filter(task=taskinfos)
        return render(request,'TaskInfo.html',{'taskinfos':taskinfos})
    else:
       messages.success(request,"You must have to login to See Task!")
       return redirect('login')           
    

#Update_Task
def updatetask(request,pk):
    if request.user.is_authenticated:
        TaskDatas=TaskDetail.objects.get(id=pk)
        form=TaskDetailForm(request.POST or None,request.FILES or None,instance=TaskDatas)
        if form.is_valid():
            form.save()
            messages.success(request,"Task Updated succesfully.....")
            return redirect('base') 
        return render(request,'Updatetask.html',{'form':form})    
    else:
       messages.success(request,"You must have to login to update task!")
       return redirect('login')     
    
#Delete_Task
def deletetask(request,pk):
    if request.user.is_authenticated:
        TaskDatas=TaskDetail.objects.get(id=pk)
        TaskDatas.delete()
        messages.success(request,"Task Deleted succesfully.....")
        return redirect('base') 
    else:
       messages.success(request,"You must have to login to delete task!")
       return redirect('login')   

#Accept_Task
def accepttask(request,pk):
    if request.user.is_authenticated:
        currentuser=request.user
        TaskDatas=TaskDetail.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Inprocess'
        TaskDatas.save()
        MyCart(user=currentuser,task=TaskDatas).save()
        messages.success(request,"Task Accepted succesfully.....")
        return redirect('base') 
    else:
       messages.success(request,"You must have to login to accept task!")
       return redirect('login')      
    


#MyCart
def MyCarts(request):
        currentuser=request.user
        Carts=MyCart.objects.filter(user=currentuser)
        return render(request,'Mycart.html',{'Carts':Carts})    



#Closed Task
def ClosedTask(request,pk):
    print("i am closed task function")
    if request.user.is_authenticated:
        currentuser=request.user
        TaskDatas=TaskDetail.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Closed'
        TaskDatas.TASK_CLOSED=currentuser
        TaskDatas.TASK_CLOSED_ON=timezone.now()
        TaskDatas.save()
        mycart=MyCart.objects.filter(task=pk)
        mycart.delete()
        messages.success(request,"Task Closed succesfully.....")
        return redirect('base') 
    else:
       messages.success(request,"You must have to login to Closed task!")
       return redirect('login')



#Remove Task
def RemoveTask(request,pk):
    if request.user.is_authenticated:
        TaskDatas=TaskDetail.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Open'
        TaskDatas.save()
        mycart=MyCart.objects.filter(task=pk)
        mycart.delete()
        messages.success(request,"Task Resolved succesfully.....")
        return redirect('base') 
    else:
       messages.success(request,"You must have to login to Removed task!")
       return redirect('login') 


#Reopen_Task
def reopentask(request,pk):
    if request.user.is_authenticated:
        TaskDatas=TaskDetail.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Reopen'
        holder=User.objects.get(username=TaskDatas.TASK_CLOSED)
        TaskDatas.save()
        MyCart(user=holder,task=TaskDatas).save()
        messages.success(request,"Task Reopen succesfully.....")
        return redirect('base') 
    else:
       messages.success(request,"You must have to login to Reopen task!")
       return redirect('login')   


#Resolved_Task
def resolvedtask(request,pk):
    if request.user.is_authenticated:
        TaskDatas=TaskDetail.objects.get(id=pk)
        TaskDatas.TASK_STATUS='Resolved'
        # holder=User.objects.get(username=TaskDatas.TASK_CLOSED)
        TaskDatas.save()
        messages.success(request,"Task Reopen succesfully.....")
        return redirect('base') 
    else:
       messages.success(request,"You must have to login to Reopen task!")
       return redirect('login')              