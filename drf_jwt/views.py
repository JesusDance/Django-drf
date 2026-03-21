from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegisterSerializer, GameListSerializer
from django_db.models import GameList

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
            "games": serializer.data
        }
        return Response(data)

