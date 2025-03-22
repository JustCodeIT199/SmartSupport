from django.shortcuts import redirect, render
from myapp.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def Basepage(request):
    return render(request,'Base.html')

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
                return render(request,'Base.html')
            else:
                messages.error(request,"Username or Password not Valid")
                return render(request,'Login.html',{'forms':forms})
    else:
        forms =LoginForm()
        return render(request,'Login.html',{'forms':forms})
    