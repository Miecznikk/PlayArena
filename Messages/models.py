from django.db import models
from Users.models import App_User
from django.utils import timezone
from django.contrib.auth.models import User


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
# Create your models here.
