from django.shortcuts import render,get_object_or_404
from .forms import RegisterForm
from .models import Position,Player,App_User
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request,'registration/sign_up.html',{'form':form})

def home_view(request):
    return render(request,'home.html',{})

def player_detail(request,id):
    player = get_object_or_404(Player,id=id)
    return render(request,'players/player_detail.html',{'player':player})

def player_ranking(request):
    import json
    players = sorted(Player.objects.all(),key=lambda x:x.get_scored_goals(),reverse=True)
    context = {
        'players':players
    }
    return render(request,'players/player_ranking.html',context=context)