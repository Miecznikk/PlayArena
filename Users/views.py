from django.shortcuts import render,get_object_or_404
from .forms import RegisterForm
from .models import Position,Player
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
            user.refresh_from_db()
            user.player.first_name = form.cleaned_data.get('first_name')
            user.player.second_name = form.cleaned_data.get('second_name')
            user.player.surname = form.cleaned_data.get('surname')
            print(Position.objects.filter(id=form.cleaned_data.get('position')))
            position = Position.objects.filter(id = form.cleaned_data.get('position'))[0]
            user.player.position = position
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request,'registration/sign_up.html',{'form':form})

def home_view(request):
    return render(request,'home.html',{})

@receiver(post_save,sender = User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Player.objects.create(user = instance)
    instance.player.save()


def player_detail(request,id):
    player = get_object_or_404(Player,id=id)
    return render(request,'players/player_detail.html',{'player':player})