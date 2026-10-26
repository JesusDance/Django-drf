from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from django_start import settings
from .models import FavoriteTeam
from .services import FootballClient


class FootballTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteTeam
        fields = ["id", "team_id", "country", "name"]


    def create(self, validated_data):
        user = validated_data.get("user")
        team_id = validated_data.get("team_id")

        client = FootballClient(url=settings.FOOTBALL_URL)

        team_db = FavoriteTeam.objects.filter(user=user, team_id=team_id).exists()
        if team_db:
            raise serializers.ValidationError("The team with given team_id exist!")

        team = client.fetch_team(team_id=team_id)

        return FavoriteTeam.objects.create(**team, user=user)






