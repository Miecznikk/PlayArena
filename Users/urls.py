from django.urls import path
from django.contrib.auth import views as v
from . import views
from .forms import UserLoginForm

app_name= 'users'

urlpatterns = [
    path('register/',views.sign_up,name='register'),
    path('login/',v.LoginView.as_view(template_name="registration/login.html",authentication_form=UserLoginForm),
         name='login')
]