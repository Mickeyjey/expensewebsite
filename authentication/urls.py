from django.urls import path
from .views import UserLogin,UserSignUp

urlpatterns = [
    path('',UserLogin.as_view(), name ="login"),
    path('signup',UserSignUp.as_view(), name ="signup"),
]
