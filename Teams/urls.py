from django.urls import path
from . import views

app_name='teams'

urlpatterns = [
    path('teams/register',views.team_register,name='team_register')
]