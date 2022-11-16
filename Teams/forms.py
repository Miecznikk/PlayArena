from django import forms

from .models import Team

class RegisterTeamForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        self.request = kwargs.pop('request')
        super(RegisterTeamForm, self).__init__(*args,**kwargs)

    class Meta:
        model = Team
        exclude = ('slug',)
        labels = {
            'name' : 'Nazwa drużyny',
            'image' : 'Zdjęcie'
        }

    def clean(self):
        cd = self.cleaned_data
        user = self.request.user.player
        if user.team is not None:
            raise forms.ValidationError('Jesteś już w drużynie, opuść ją aby założyć nową')
        return cd