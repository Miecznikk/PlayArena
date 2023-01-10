from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from .models import Match

def all_matches(request):
    matches = Match.objects.all()
    return render(request,'matches/all_matches.html',{'matches':matches})

@login_required(login_url='/login')
def my_matches(request):
    matches = Match.objects.filter(Q(team1=request.user.player.team) | Q(team2=request.user.player.team))
    return render(request,'matches/my_matches.html',{'matches':matches})
# Create your views here.
