from django.urls import path
from . import views

app_name = 'matches'

urlpatterns = [
    path('matches/',views.all_matches,name='all_matches'),
    path('matches/my_matches',views.my_matches,name='my_matches'),
]
