from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
from Teams.models import Team
from random import choice
from django.urls import reverse

def get_name(self):
    return f'{self.first_name} {self.last_name}'

def isinst(self):
    if hasattr(self,'player'):
        return 'player'
    elif hasattr(self,'referee'):
        return 'referee'
    return 'none'

User.add_to_class("__str__",get_name)
User.add_to_class("isinst",isinst)

class Position(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class App_User(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    second_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    mod = models.BooleanField(default=False,null=False)

    image = models.ImageField(upload_to='images/users', null=False, default='images/users/default_profile.png')

    def __str__(self):
        return f'{self.first_name} {self.second_name+" " if self.second_name else " "}{self.last_name}'

class Player(App_User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE,null=True,blank=True)
    shirt_number = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(99)],null=True,blank=True)
    team = models.ForeignKey(Team,on_delete=models.SET_NULL,null=True,blank=True)
    captain = models.BooleanField(null=False,default=False)

    def get_absolute_url(self):
        return reverse('users:player_detail',args=[self.id])

    def get_scored_goals(self):
        from Matches.models import Goal
        return len(Goal.objects.filter(scorer = self))

    def get_motm(self):
        from Matches.models import Match
        return len(Match.objects.filter(motm = self))


class Referee(App_User):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    @classmethod
    def get_suitable_referee(cls):
        return choice(cls.objects.all())


# Create your models here.

