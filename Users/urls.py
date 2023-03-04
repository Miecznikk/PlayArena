from django.urls import path
from django.contrib.auth import views as v
from . import views
from .forms import UserLoginForm

app_name= 'users'

urlpatterns = [
    path('register/',views.sign_up,name='register'),
    path('login/',v.LoginView.as_view(template_name="registration/login.html",authentication_form=UserLoginForm),
         name='login'),
    path('players/<int:id>',views.player_detail,name='player_detail'),
    path('players/ranking',views.player_ranking,name='player_ranking'),
    path('players/profile',views.update_profile,name='profile')
]