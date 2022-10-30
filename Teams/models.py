from django.db import models

class Team(models.Model):
    name = models.CharField(unique=True,max_length=30)
    slug = models.SlugField(unique=True,max_length=30)
    image = models.ImageField(upload_to='images/teams')

    def __str__(self):
        return self.name




# Create your models here.
