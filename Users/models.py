from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from Teams.models import Team
from django.contrib.auth.models import User
from django.urls import reverse

def get_name(self):
    return f'{self.first_name} {self.last_name}'

User.add_to_class("__str__",get_name)

class Position(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class App_User(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    second_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/users', null=False, default='images/default_profile_picture')
    mod = models.BooleanField(default=False,null=False)

    def __str__(self):
        return f'{self.first_name} {self.second_name+" " if self.second_name else ""}{self.last_name + " [ADMIN]" if self.mod else self.last_name}'


class Player(App_User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE,null=True,blank=True)
    shirt_number = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(99)],null=True,blank=True)
    team = models.ForeignKey(Team,on_delete=models.SET_NULL,null=True,blank=True)
    captain = models.BooleanField(null=False,default=False)

    def get_absolute_url(self):
        return reverse('users:player_detail',args=[self.id])

class Referee(App_User):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

# Create your models here.

