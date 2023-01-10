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

# Create your models here.
