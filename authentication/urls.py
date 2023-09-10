from django.urls import path
from .views import UserLogin,UserSignUp, ResetPassword

urlpatterns = [
    path('',UserLogin.as_view(), name ="login"),
    path('signup',UserSignUp.as_view(), name ="signup"),
    path('reset',ResetPassword.as_view(), name ="reset"),
]
