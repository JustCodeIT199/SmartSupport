from django.shortcuts import redirect, render
from myapp.forms import LoginForm,RegisterForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from myapp.models import UserProfile

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
    
#LogoutView
def LogoutView(request):
    logout(request)
    messages.error(request,"⚠️ You have been successfully logged out. See you again soon!")
    return redirect('login')

#Register
def RegisterView(request):
    if request.method =='POST':
        Register_forms =RegisterForm(request.POST)
        UserProfile_forms =UserProfileForm(request.POST)
        if Register_forms.is_valid() and UserProfile_forms.is_valid():
            Registerforms=Register_forms.save()
            UserProfileforms=UserProfile_forms.save(commit=False)
            Address=UserProfile_forms.cleaned_data['Address']
            RegistratioNo=UserProfile_forms.cleaned_data['RegistratioNo']
            Year=UserProfile_forms.cleaned_data['Year']
            Department=UserProfile_forms.cleaned_data['Department']
            profile=UserProfile(User=Registerforms,Address=Address,RegistratioNo=RegistratioNo,Year=Year,Department=Department)
            profile.save()
            messages.success(request,"✅ You have been Registered Successfully!")
            return redirect('login')
        else:
            messages.error(request,"⚠️ You have not enter correct data!")
            return redirect('register')
    else:
        Register_forms=RegisterForm()
        UserProfile_forms=UserProfileForm()

        return render(request,'Register.html',{'Register_forms':Register_forms,'UserProfile_forms':UserProfile_forms})


