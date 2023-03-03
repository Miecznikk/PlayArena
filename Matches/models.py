from django.db import models
from Users.models import Player,Referee
from Teams.models import Team

class Stadium(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.location}'

class Match(models.Model):
    team1 = models.ForeignKey(Team,related_name='team1',on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team,related_name='team2',on_delete=models.CASCADE)

    stadium = models.ForeignKey(Stadium,null=True,on_delete=models.SET_NULL)

    referee = models.ForeignKey(Referee,null=True,related_name='referee',on_delete=models.SET_NULL)

    motm = models.ForeignKey(Player,null=True,related_name='motm',on_delete=models.SET_NULL)

    date = models.DateField(null=False)
    status = models.BooleanField(default=False,null=False)

    def __str__(self):
        return f'{self.team1} - {self.team2} | {self.stadium} | {self.date} | {self.get_score() if self.status else "Do rozegrania"}'

    def get_goals(self):
        goals1 = len(Goal.objects.filter(match=self, team=self.team1))
        goals2 = len(Goal.objects.filter(match=self, team=self.team2))

        return goals1, goals2

    def get_score(self):
        goals1,goals2 = self.get_goals()
        return f'{goals1} : {goals2}'

    def get_winner(self):
        goals1,goals2 = self.get_goals()
        if goals1 > goals2:
            return self.team1
        elif goals1 < goals2:
            return self.team2
        return None

    @classmethod
    def get_matches_day_stadium(cls,_date,_stadium):
        return cls.objects.filter(date=_date,stadium=_stadium)


class Goal(models.Model):
    scorer = models.ForeignKey(Player,null=True,on_delete=models.SET_NULL)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.scorer} - {self.match}'


# Create your models here.
