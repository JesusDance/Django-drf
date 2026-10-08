from django.contrib.auth.models import User
from rest_framework import serializers

from django_db.models import Game


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.email_user(
            subject="Welcome",
            message="Your account was created",
            from_email="jiesusdance@gmail.com",
        )
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


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]



class GameModelSerializer(serializers.ModelSerializer):
    genre_display = serializers.CharField(source="get_genre_display", read_only=True)

    class Meta:
        model = Game
        fields = ["id", "name", "genre", "genre_display", "description", "wiki_page"]
