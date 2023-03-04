from django.shortcuts import render,get_object_or_404
from .forms import RegisterForm,ProfileEditForm
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
    players = sorted(Player.objects.all(),key=lambda x:x.get_scored_goals(),reverse=True)
    context = {
        'players':players
    }
    return render(request,'players/player_ranking.html',context=context)

def update_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST,request.FILES,instance=request.user.player)
        if form.is_valid():
            request.user.first_name = form.cleaned_data.get('first_name')
            request.user.last_name = form.cleaned_data.get('last_name')
            request.user.save()
            form.save()
            return redirect('home')

    else:
        player = get_object_or_404(Player,id = request.user.player.id)
        initial_player_values = {
            'first_name':player.first_name,
            'second_name':player.second_name,
            'last_name':player.last_name,
            'shirt_number':player.shirt_number,
            'image':player.image
        }
        form = ProfileEditForm(initial=initial_player_values)
    return render(request,'players/profile.html',{'form':form})