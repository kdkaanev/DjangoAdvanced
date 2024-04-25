from django.shortcuts import render
from django.contrib.auth import views as auth_views
# Create your views here.
class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'