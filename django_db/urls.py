from django.urls import path

from .views import (
    SignUpView,
    UserLogin,
    UserLogout,
    UserUpdate,
    Delete,
    client_view,
    GameView,
    GetGameList,
    GetGame,
    GameUpdate,
    GameDelete,
)

urlpatterns = [
    path("", SignUpView.as_view(), name="user-view"),
    path("login/", UserLogin.as_view(), name="login"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("update/", UserUpdate.as_view(), name="update"),
    path("delete/", Delete.as_view(), name="delete"),
    path("accounts/profile/", client_view, name="profile"),
    path("client/game/", GameView.as_view(), name="game-view"),
    path("get-gamelist/", GetGameList.as_view(), name="game-list"),
    path("get-game/<int:game_id>/", GetGame.as_view(), name="get-game"),
    path("game-update/<int:game_id>/", GameUpdate.as_view(), name="game-update"),
    path("game-delete/<int:game_id>/", GameDelete.as_view(), name="game-delete"),
    # path('get_game/<int:game_id>/', get_game, name='get_game')
]
