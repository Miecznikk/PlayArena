from django import forms
from datetime import date
from .models import Message, Invite, Challenge
from django.contrib.auth.models import User
from Teams.models import Team
from Matches.models import Match

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
        labels = {
            'challenged_team': 'Drużyna',
            'stadium': 'Boisko',
            'date': 'Data'
        }
        widgets = {
            'date':DateInput()
        }

    def clean(self):
        cd = self.cleaned_data
        matches_that_day = Match.get_matches_day_stadium(cd.get('date'),cd.get('stadium'))

        if len(matches_that_day) > 0:
            raise forms.ValidationError('Tego dnia odbywa się już mecz na tym boisku')

        if cd.get('date') <= date.today():
            raise forms.ValidationError('Pomiędzy dniem dzisiejszym a meczowym musi być co najmniej jeden dzień')

        if cd.get('challenged_team') == self.team:
            raise forms.ValidationError('Nie możesz rzucić wyzwania samemu sobie!')
