from django.urls import path
from .views import UserView, client_view, GameView, GetGame, get_game

urlpatterns = [
    path('', UserView.as_view(), name='user-view'),
    path('client/', client_view, name='client-view'),
    path('client/game/', GameView.as_view(), name='game-view'),
    path('get-gamelist/', GetGame.as_view(), name='game-list'),
    path('get-game/', get_game, name='get-game'),
]