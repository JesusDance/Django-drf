from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import FavoriteTeam
from .serializer import FootballTeamSerializer


class FootballTeamView(ModelViewSet):
    serializer_class = FootballTeamSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        return FavoriteTeam.objects.filter(user=self.request.user).order_by("-id")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)