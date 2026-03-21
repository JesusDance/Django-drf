from rest_framework import serializers
from django_db.models import Client, Game, GameList
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

        # def create(self, validated_data):
        #     password = validated_data.pop("password")
        #     user = User(**validated_data)
        #     user.set_password(password)
        #     user.save()
        #     return user

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user


class ClientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class GameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class GameListSerializer(serializers.ModelSerializer):
    gamer = serializers.CharField(source="gamer.username", read_only=True)
    game_list = GameModelSerializer(many=True, read_only=True)

    class Meta:
        model = GameList
        fields = "__all__"


