from django.db import models

from Teams.models import Team
from Players.models import Player


class Stadium(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.location}'

class Match(models.Model):
    team1 = models.ForeignKey(Team,related_name='team1',on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team,related_name='team2',on_delete=models.CASCADE)

    stadium = models.ForeignKey(Stadium,null=True,on_delete=models.SET_NULL)

    date = models.DateField(null=False)
    status = models.BooleanField(default=False,null=False)

    def __str__(self):
        return f'{self.team1} - {self.team2}'

class Goal(models.Model):
    scorer = models.ForeignKey(Player,on_delete=models.CASCADE)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.scorer} - {self.match}'


# Create your models here.
