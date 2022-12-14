from django import forms
from .models import Player,Position
from Teams.models import Team
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import transaction

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło',widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=True,label="Imię")
    second_name = forms.CharField(max_length=30,required=False,label="Drugie imię")
    last_name = forms.CharField(max_length=30,required=True,label="Nazwisko")

    username = forms.CharField(max_length=30,required=True,label="Nazwa użytkownika")
    password1 = forms.CharField(label='Hasło',strip=False,widget=forms.PasswordInput())
    password2 = forms.CharField(label='Potwierdź hasło', strip=False, widget=forms.PasswordInput())

    position = forms.ChoiceField(label = 'Pozycja',
                                 choices=(('1','Bramkarz'),('2','Obrona'),('3','Pomoc'),('4','Atak')),required=True)

    class Meta:
        model = User
        fields = ['username','first_name','second_name','last_name','password1','password2','position']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        cd = self.cleaned_data
        fn = cd.get('first_name')
        sn = cd.get('second_name')
        ln = cd.get('last_name')
        position = Position.objects.filter(id=cd.get('position'))[0]
        player = Player.objects.create(user=user,first_name= fn,second_name=sn,last_name=ln,position=position)
        return user
