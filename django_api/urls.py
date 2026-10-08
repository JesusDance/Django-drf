from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CreateUser, GameViewSet, user_login, UpdateUser, DeleteUser

router = SimpleRouter()
router.register(r"games", GameViewSet, "games")

urlpatterns = [
    path("", include((router.urls, "rest_api"), namespace="rest_api")),
    path("create-user/", CreateUser.as_view(), name="create-user"),
    path("update-user/", UpdateUser.as_view(), name="update-user"),
    path("delete-user/", DeleteUser.as_view(), name="delete-user"),
    path("api-login/", user_login, name="api-login"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
