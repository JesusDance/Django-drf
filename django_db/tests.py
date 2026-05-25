from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase, Client

from .models import Game


class PrivateModelTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="Steve",
                                                         password="test_pass12345",
                                                         email="test@gmail.com")
        self.client.force_login(self.user)

        Game.objects.create(name="cs-go", description="some_old_game",
                            user=self.user)
        Game.objects.create(name="cs-go2", description="some_old_game2",
                            user=self.user)

    def test_retrieve_model(self):
        response = self.client.get("/get-gamelist/")

        games = Game.objects.filter(user=self.user).order_by("-id")
        print(response.context["object_list"])
        print(games)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(list(response.context["object_list"]), list(games))

    def test_model_exists(self):
        payload = {"name": "test_name", "description": "some_text"}
        response = self.client.post("/client/game/", payload)

        exists_game = Game.objects.filter(name=payload["name"], user=self.user).exists()

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(exists_game)

    def test_no_permission(self):
        new_client = Client()  # клієнт без логіну (анонімний користувач)
        response = new_client.get("/get-gamelist/")  # робимо запит

        # редірект бо LoginRequiredMixin перенаправляє по дефолту на /accounts/login/, але в мене
        # LOGIN_URL = "login" (reverse("login")
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, "/login/?next=/get-gamelist/")

    def test_no_permission_for_user2(self):
        client2 = Client()
        payload = {"username": "user2", "password": "12345", "email": "test2@gmail.com"}
        user2 = get_user_model().objects.create_user(**payload)

        client2.force_login(user2)
        response = client2.get("/get-game/1/")

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)


class PublicTest(TestCase):
    def setUp(self):
        self.client = Client() # клієнт без логіну (анонімний користувач)

    def test_signup(self):
        payload = {"username": "test_user",
                   "password1": "test_pass123", #UserCreationForm має такі поля
                   "password2": "test_pass123", #UserCreationForm має такі поля
                   "email": "test@gmail.com"}

        response = self.client.post("/", payload) # робимо запит
        exists_user = User.objects.filter(username=payload["username"]).exists()

        # FOUND тому що success_url redirect -> accounts/profile/
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(exists_user)

    def test_create_invalid_user(self):
        payload = {"username": "", "password1": ""}
        response = self.client.post("/", payload)
        print(response.context["form"])

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertFalse(response.context["form"].is_valid())
        self.assertFormError(response.context["form"], "username",
                             "This field is required.")