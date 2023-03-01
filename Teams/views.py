from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .forms import RegisterTeamForm
from Users.models import Player
from Teams.models import Team

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

def teams(request):
    teams = Team.objects.all()
    return render(request,'teams/all_teams.html',{'teams':teams})

def team_detail(request,slug):
    team = get_object_or_404(Team,slug=slug)
    players = Player.objects.filter(team=team)
    return render(request,'teams/team_detail.html',{'team':team,'players':players})

def table_view(request):
    teams = sorted(Team.objects.all(),key=lambda x: x.get_points(),reverse=True)
    context = {
        'teams': teams
    }
    return render(request,'teams/table.html',context=context)
# Create your views here.
