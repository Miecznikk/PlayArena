from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from Teams.models import Team

class Position(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Player(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    second_name = models.CharField(max_length=30,null=True,blank=True)
    surname = models.CharField(max_length=30)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    shirt_number = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(99)])
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/players',null=False,default='images/default_profile_picture')
    captain = models.BooleanField(null=False,default=False)

    def __str__(self):
        if self.second_name is not None:
            return f'{self.first_name} {self.second_name} {self.surname}'
        else:
            return f'{self.first_name} {self.surname}'

# Create your models here.
