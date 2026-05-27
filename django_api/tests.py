from django.contrib.auth import \
    get_user_model  # беремо модель користувача (не хардкодимо auth.User)
from django.test import TestCase
from django.urls import reverse  # будує URL по name з urls.py
from rest_framework import status
from rest_framework.test import APIClient

from django_db.models import Game
from .serializers import GameModelSerializer

MODEL_URL = reverse('rest_api:games-list')
print(reverse('rest_api:games-list'))
print(MODEL_URL)

class PublicApiTest(TestCase):
    def setUp(self):
        # клієнт без логіну (анонімний користувач)
        self.client = APIClient()

    def test_login_required(self):
        # робимо запит до API
        response = self.client.get(MODEL_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateModelApiTests(TestCase):
    def setUp(self):
        #create real user (НЕ create(), тільки create_user → password hashing)
        payload = {"username": "test_user",
                   "password": "test_pass12345",
                   "email": "test@gmail.com"}
        self.user = get_user_model().objects.create_user(**payload)

        Game.objects.create(name="test_game", user=self.user)
        Game.objects.create(name="test_game2", user=self.user)

        self.client = APIClient()
        self.client.force_authenticate(self.user) #simulate logged-in user

    #отримуємо данні
    def test_retrieve_model(self):
        # створюємо дані в БД (2 записи гри)
        Game.objects.create(name="test_game3", user=self.user)
        Game.objects.create(name="test_game4", user=self.user)

        # робимо запит до API
        response = self.client.get(MODEL_URL)
        #витягуємо данні з бд тільки цього користувача, і серіалізуємо в json
        models = Game.objects.filter(user=self.user).order_by("-name")
        serializer = GameModelSerializer(models, many=True) # бо це список, не один об'єкт

        # перевірка що API відповів успішно
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # порівнюємо що прийшло з API і що в БД
        self.assertEqual(response.data["results"], serializer.data)

    def test_create_invalid_user(self):
        new_client = APIClient()
        response = new_client.post("/create-user/", {"username": ""})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_no_access_to_games(self):
        new_client = APIClient()
        payload = {"username": "test_user2",
                   "password": "test_pass22345",
                   "email": "test2@gmail.com"}
        user2 = get_user_model().objects.create_user(**payload)
        new_client.force_authenticate(user2)

        response = new_client.get("/games/1/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)