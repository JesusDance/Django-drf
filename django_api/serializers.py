from django.contrib.auth.models import User
from rest_framework import serializers

from django_db.models import Game


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

        # def create(self, validated_data):
        #     password = validated_data.pop("password")
        #     user = User(**validated_data)
        #     user.set_password(password)
        #     user.save()
        #     return user


# class ClientModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = "__all__"


class GameModelSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(source="get_genre_display")

    class Meta:
        model = Game
        fields = ["id", "name", "genre", "description", "wiki_page"]
