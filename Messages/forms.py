from django import forms
from .models import Message
from django.contrib.auth.models import User

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
