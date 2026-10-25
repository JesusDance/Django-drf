from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializer import FootballTeamSerializer


class FootballTeamView(CreateAPIView):
    serializer_class = FootballTeamSerializer
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)