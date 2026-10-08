from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField
from django.utils.translation import gettext_lazy as _

SELECT_GENRE = [
    ("1", "rpg"),
    ("2", "shooter"),
    ("3", "strategy"),
]


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=64, unique=True, null=True)
    phone = PhoneField(blank=True, help_text=_("Please enter your phone number"))
    # email = models.EmailField(unique=True, max_length=64, null=True)
    photo = models.ImageField(_("photo"), blank=True, help_text=_("Please put in your photo"))
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    genre = models.CharField(
        max_length=64,
        blank=True,
        choices=SELECT_GENRE,
        help_text=_("Please select genre of game"),
    )
    description = models.TextField(max_length=200, blank=True)
    wiki_page = models.URLField(default="https://wikipedia.com", blank=True)

    def __str__(self):
        return f"{self.name}"


class GameList(models.Model):
    gamer = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    game_list = models.ManyToManyField(Game, verbose_name=_("Games for PC"))

    def __str__(self):
        return f"{self.id}_{self.gamer.username}"
