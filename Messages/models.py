from django.db import models
from Users.models import App_User
from django.utils import timezone
from Teams.models import Team
from django.contrib.auth.models import User
from Matches.models import Stadium


class Message(models.Model):
    title = models.CharField(max_length=50,blank=False,null=False)
    description = models.TextField(max_length=500,null=False,blank=False)
    created = models.DateTimeField()

    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')

    def save(self,*args,**kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(Message,self).save(*args,**kwargs)

    def check_instance(self):
        if hasattr(self,'invite'):
            return 'invite'
        elif hasattr(self,'challenge'):
            return 'challenge'
        return 'message'

class Invite(Message):
    invited_to = models.ForeignKey(Team,on_delete=models.CASCADE)

class Challenge(Message):
    challenged_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='challenged_team')
    challenging_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='challenging_team')

    stadium = models.ForeignKey(Stadium,null=True,on_delete=models.SET_NULL)
    date = models.DateField()
# Create your models here.
