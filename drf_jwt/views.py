"""
JWT authentication app.

This app contains authentication-related endpoints:
- user registration
- JWT token issuing
- token refresh flow

Business logic is intentionally minimal.
Core domain logic lives in django_api / django_db.
"""

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from django_db.models import GameList
from .serializers import UserRegisterSerializer, GameListSerializer


class UserRegisterView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "User created successfully"})


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        game_list = GameList.objects.filter(gamer=self.request.user)
        serializer = GameListSerializer(game_list, many=True)
        data = {
            "username": request.user.username,
            "email": request.user.email,
            "games": serializer.data,
        }
        return Response(data)
