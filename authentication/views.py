from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import json
from django.http import Http404
from django.http import JsonResponse
from django.core import serializers

class UserLogin(View):
    def get(self,request):
        return render(request,"auths/login.html")
    
    def post(self,request):
        data = request.POST
        if User.objects.filter(username=data["username"]).exists():
            user = User.objects.filter(username=data["username"])
            if user.filter(password=data["password"]).exists():
                person = user.filter(password=data["password"]).first()
                return JsonResponse({"user":person})
            else:
                return JsonResponse({"error":"wrong password"})
        else:
            return Http404("Not a registered user")
        

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