from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CreateUser, GameViewSet, user_login

router = SimpleRouter()
router.register(r"games", GameViewSet, "games")

urlpatterns = [
    path("", include((router.urls, "rest_api"), namespace="rest_api")),
    path("create-user/", CreateUser.as_view(), name="create-user"),
    path("api-login/", user_login, name="api-login"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
