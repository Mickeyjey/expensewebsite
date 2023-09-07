from django.urls import path
from . import views

urlpatterns = [
    path('',views.signIn, name ="expenses"),
    path('register',views.register, name ="expenses"),
    path('reset',views.resetPassword, name ="expenses"),
    path('set',views.setPassword, name ="expenses"),
]
