from django.urls import path
from . import views

app_name = 'errors'

urlpatterns = [
    path('errors/stadium_occupied/?<int:opposing_captain_id>',views.stadium_occupied_view,name='stadium_occupied')
]