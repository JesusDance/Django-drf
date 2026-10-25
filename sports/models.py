from django.db import models
from django.contrib.auth.models import User


class FavoriteTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Name of the football team"
    )
    country = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Country of the football team"
    )
    team_id = models.IntegerField(blank=True, null=True)
    logo = models.URLField(blank=True, null=True)