from django import forms

from .models import Message, Invite, Challenge
from django.contrib.auth.models import User
from Teams.models import Team

class SendMessage(forms.ModelForm):

    receiver = forms.ModelChoiceField(required=True,label="Odbiorca",queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['receiver','title','description']
        labels = {
            'receiver' : 'Odbiorca',
            'title' : 'Tytuł',
            'description': 'Treść'
        }

    def __init__(self,*args,**kwargs):
        self.user = kwargs.pop('user')
        super(SendMessage, self).__init__(*args,**kwargs)
        self.fields['receiver'].queryset = User.objects.all().exclude(id = self.user.id)

class DateInput(forms.DateInput):
    input_type = 'date'

class SendInvite(forms.ModelForm):
    receiver = forms.ModelChoiceField(required=True,label="Odbiorca",queryset=User.objects.filter(player__team=None).exclude(player=None))

    class Meta:
        model = Invite
        fields = ['receiver']

class SendChallenge(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        self.team = kwargs.pop('team')
        super(SendChallenge, self).__init__(*args,**kwargs)

    class Meta:
        model = Challenge
        fields = ['challenged_team','stadium','date']

        widgets = {
            'date':DateInput()
        }