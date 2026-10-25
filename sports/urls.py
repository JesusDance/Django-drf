from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import FootballTeamView
# router = SimpleRouter()
# router.register(r"api/football", FootballTeamView, "football")

urlpatterns = [
    #path("", include((router.urls, "rest_api"), namespace="rest_api")),
    path("api/football/", FootballTeamView.as_view(), name="football")
]