from django.shortcuts import render

# Create your views here.
def signIn(request):
    return render(request,"auths/login.html")

def register(request):
    return render(request,"auths/register.html")

def resetPassword(request):
    return render(request,"auths/resetpasword.html")

def setPassword(request):
    return render(request,"auths/setpassword.html")