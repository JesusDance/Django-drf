from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput

from .models import Client, Game


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["phone", "photo", "age", "birthday"] #замість "__all__" якщо в майбутньому добавиться службове поле
        #exclude = ["user"]
        widgets = {"birthday": DateInput(attrs={"type": "date"})}


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ["name", "genre", "description", "wiki_page"]
