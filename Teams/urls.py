from django.urls import path
from . import views

app_name='teams'

urlpatterns = [
    path('teams/register',views.team_register,name='team_register'),
    path('teams/',views.teams,name='teams'),
    path('teams/table',views.table_view,name='table'),
    path('teams/<slug:slug>',views.team_detail,name='team_detail'),
    path('teams/<slug:slug>/leave_team',views.leave_team,name='leave_team'),
]
