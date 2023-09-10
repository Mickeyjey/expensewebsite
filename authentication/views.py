from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse

class UserLogin(View):
    def get(self,request):
        return render(request,"auths/login.html")
    
    def post(self,request):
        data = request.POST
        if User.objects.filter(username=data["username"]).exists():
            user = User.objects.get(username=data["username"])       
            if user.check_password(raw_password=data["password"]):
                return render(request,"expenses/index.html")
            else:
                return JsonResponse({"error":"wrong password"})
        else:
            return JsonResponse({"error":"entirely wrong"})
        

class UserSignUp(View):
    def get(self,request):
        return render(request,"auths/register.html")
    
    def post(self,request):
        data = request.POST
        if  User.objects.filter(username=data["username"]).exists():
            return JsonResponse({"error":"User already exists"})
        else:
            user = User.objects.create_user(data["username"], data["email"],data["password"])
            user.save()
            return render(request,"expenses/index.html")

class ResetPassword(View):
    def get(self,request):
        return render(request,"auths/resetpasword.html")
    
    def post(self,request):
        data = request.POST
        if "email" in data:
            if  User.objects.filter(email=data["email"]).exists():
                user = User.objects.get(email=data["email"])
                send_mail(
                    subject="verify email",
                    message="1234",
                    from_email="koonimoapaa@gmail.com",
                    recipient_list=[user.email],
                    fail_silently=True
                    
                )
                return render(request,"auths/setpassword.html")
            else:
                return JsonResponse({"error":"no user with such email"})
        
        if "password" in data:
            if  User.objects.filter(email=data["code"]).exists():
                user = User.objects.get(email=data["code"])
                user.set_password(data["password"])
                user.save()
                return render(request,"expenses/index.html")
            else:
                return JsonResponse({"error":"no user with such email"})
            