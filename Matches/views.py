from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q

from Users.models import Player
from .models import Match,Goal

def all_matches(request):
    matches = Match.objects.all()
    return render(request,'matches/all_matches.html',{'matches':matches})

@login_required(login_url='/login')
def my_matches(request):
    if hasattr(request.user,'player'):
        matches = Match.objects.filter(Q(team1=request.user.player.team) | Q(team2=request.user.player.team))
    else:
        matches = Match.objects.filter(referee=request.user.referee)
    matches_played = matches.filter(date__lt=date.today())
    matches_upcoming = matches.filter(date__gt=date.today())
    return render(request,'matches/my_matches.html',{'matches_played':matches_played,'matches_upcoming':matches_upcoming})

def post_score(request,id):
    match = get_object_or_404(Match,id=id)
    players1 = Player.objects.filter(team = match.team1)
    players2 = Player.objects.filter(team = match.team2)

    players_ids = [player.id for player in players1 | players2]

    if request.method == "POST":
        motm = Player.objects.filter(id=request.POST.get("motm")).first()
        match.motm = motm
        for player in players1 | players2:
            goals_scored = int(request.POST.get(str(player.id)))
            for i in range(goals_scored):
                Goal.objects.create(scorer=player,team=player.team,match= match)
        match.status = True
        match.save()
        return redirect('matches:my_matches')

    context = {
        'match':match,
        'players1':players1,
        'players2':players2,
        'players_ids':players_ids
    }
    return render(request,'matches/post_score.html',context=context)