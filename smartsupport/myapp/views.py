from django.shortcuts import render

# Create your views here.
def Basepage(request):
    return render(request,'Base.html')

def LoginView(request):
    return render(request,'Login.html')
    