from django.db import models
from django.urls import reverse

class Team(models.Model):
    name = models.CharField(unique=True,max_length=30)
    slug = models.SlugField(unique=True,max_length=30)
    image = models.ImageField(upload_to='images/teams')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teams:team_detail',args=[self.slug])

# Create your models here.
