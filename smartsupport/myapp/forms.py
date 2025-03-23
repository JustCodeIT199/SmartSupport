from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from myapp.models import UserProfile
#login form 
class LoginForm(forms.Form):
    username=forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#RegisterForm
class RegisterForm(UserCreationForm):
    first_name=forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username=forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2')

#UserProfile Form
class UserProfileForm(forms.ModelForm):
    Address=forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    RegistratioNo=forms.CharField(label='RegistratioNo', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Year=forms.CharField(label='Year', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Department=forms.CharField(label='Department', widget=forms.TextInput(attrs={'class': 'form-control'}))

   
    class Meta:
        model=UserProfile
        fields=('Address','RegistratioNo','Year','Department')