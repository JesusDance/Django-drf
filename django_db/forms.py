from django.forms import ModelForm, DateInput
from .models import Client, Game
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserForm2(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        widgets = {'birthday': DateInput(attrs={'type': 'date'})}


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = "__all__"





