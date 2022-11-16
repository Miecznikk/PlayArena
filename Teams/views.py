from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .forms import RegisterTeamForm
from Users.models import Player

@login_required(login_url='/login')
def team_register(request):
    if request.method == "POST":
        form = RegisterTeamForm(request.POST,request.FILES,request=request)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.instance.slug = slugify(name)
            team = form.save()
            player = Player.objects.filter(user = request.user).first()
            player.team = team
            player.captain = True
            player.save()
            return redirect('/home')
    else:
        form = RegisterTeamForm(request=request)

    return render(request,'teams/register.html',{'form':form})

# Create your views here.
