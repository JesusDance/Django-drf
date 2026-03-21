from django.urls import path, include
from .views import CreateUser, GameViewSet, GameListViewSet, user_login
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'games', GameViewSet, 'games')
router.register(r'games-list', GameListViewSet, 'games-list')

urlpatterns = [
    path('', include(router.urls)),
    path('create-user/', CreateUser.as_view(), name='create-user'),
    path('login/', user_login, name='login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
