from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import json
from django.http import Http404
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate

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
        data = json.load(request)
        email = data["email"]
        if(User.objects.filter("email"==email).exists()):
            return 
        else:
            return JsonResponse({"error":"something happens"})