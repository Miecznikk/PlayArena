from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(unique=True,max_length=30)
    slug = models.SlugField(unique=True,max_length=30)
    image = models.ImageField(upload_to='images/teams')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teams:team_detail',args=[self.slug])

    def get_captain(self):
        cpt = User.objects.all().exclude(player=None).filter(player__team=self,player__captain=True).first()
        return cpt

    def get_matches(self):
        from Matches.models import Match
        return Match.objects.filter(status = True,team1 = self) | Match.objects.filter(status = True,team2 = self)

    def get_wins(self):
        return sum(list(map(lambda x:x.get_winner()==self,self.get_matches())))

    def get_loses(self):
        def is_lost(match):
            return match.get_winner() not in (None,self)

        return sum(list(map(is_lost,self.get_matches())))

    def get_draws(self):
        return len(self.get_matches()) - self.get_wins() - self.get_loses()

    def get_goals_scored(self):
        from Matches.models import Goal
        return len(Goal.objects.filter(team = self))

    def get_goals_lost(self):
        from Matches.models import Match,Goal
        goals = []
        matches = Match.objects.filter(team1 = self) | Match.objects.filter(team2 = self)
        for match in matches:
            goals+=Goal.objects.filter(match = match)

        return len(goals) - self.get_goals_scored()

    def get_points(self):
        return self.get_wins() * 3 + self.get_draws()


# Create your models here.
