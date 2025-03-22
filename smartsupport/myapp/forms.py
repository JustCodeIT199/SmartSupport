from django import forms

#login form 
class LoginForm(forms.Form):
    username=forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))