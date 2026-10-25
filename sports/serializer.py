from rest_framework import serializers

from django_start import settings
from .models import FavoriteTeam
from .services import FootballClient


class FootballTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTeam
        fields = ["team_id", "country", "name"]


    def create(self, validated_data):
        user = validated_data.pop("user")

        client = FootballClient(url=settings.FOOTBALL_URL)
        team = client.fetch_team(validated_data["team_id"])

        return FavoriteTeam.objects.create(**team, user=user)

