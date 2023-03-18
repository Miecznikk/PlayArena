from django import forms

from .models import Team
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class RegisterTeamForm(forms.ModelForm):

    capthca = ReCaptchaField(widget=ReCaptchaV2Checkbox,label="")

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