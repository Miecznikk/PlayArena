from django import forms
from .models import Player
from Teams.models import Team
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło',widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=True,label="Imię")
    second_name = forms.CharField(max_length=30,required=False,label="Drugie imię")
    surname = forms.CharField(max_length=30,required=True,label="Nazwisko")

    username = forms.CharField(max_length=30,required=True,label="Nazwa użytkownika")
    password1 = forms.CharField(label='Hasło',strip=False,widget=forms.PasswordInput())
    password2 = forms.CharField(label='Potwierdź hasło', strip=False, widget=forms.PasswordInput())

    position = forms.ChoiceField(label = 'Pozycja',
                                 choices=(('1','Bramkarz'),('2','Pomoc'),('3','Obrona'),('4','Atak')),required=True)

    class Meta:
        model = User
        fields = ['username','first_name','second_name','surname','password1','password2','position']