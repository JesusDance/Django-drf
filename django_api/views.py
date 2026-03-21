from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django_db.models import Game, GameList
from .serializers import UserSerializer, GameModelSerializer, GameListSerializer


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


@api_view(["POST"])
@permission_classes((AllowAny,))
def user_login(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({"error": "Invalid username or password!"})

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"access token": token.key}, HTTP_200_OK)


class GameViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GameModelSerializer
    queryset = Game.objects.all()


class GameListViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GameListSerializer

    def get_queryset(self):
        queryset = GameList.objects.filter(gamer=self.request.user)
        return queryset




