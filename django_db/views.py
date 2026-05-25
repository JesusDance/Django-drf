from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView, DeleteView, \
    UpdateView

from .forms import ClientForm, GameForm, UserForm
from .models import Game, Client


class SignUpView(FormView):
    form_class = UserForm
    template_name = "registration/sign_up.html"
    success_url = "/accounts/profile/"

    def form_valid(self, form: UserForm) -> HttpResponse:
        user = form.save()

        #authenticate() зайвий(зайвий запит в бд і перевірка pass_hash)/створення юзера нового
        # user = authenticate(username=form.cleaned_data["username"],
        #                     password=form.cleaned_data["password1"])

        login(self.request, user)

        messages.success(self.request, "User created successfully")

        return super().form_valid(form)


@login_required
def client_view(request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        client = form.save(commit=False)
        client.user = request.user #без цього кожен в сесії бачив список юзерів
        client.save()
        messages.success(request, "User profile created successfully")
        return redirect("game-view")

    return render(request, template_name="registration/sign_up.html", context={"form": form})


class UserLogin(LoginView):
    next_page = "game-view"


class UserLogout(LoginRequiredMixin, LogoutView):
    next_page = "login"

    def post(self, request, *args, **kwargs):
        messages.info(self.request, "You are logged out")
        return super().post(request, *args, **kwargs)


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "registration/sign_up.html"
    success_url = "/accounts/profile/"

    def get_object(self):
        return self.request.user.client

    def form_valid(self, form):
        messages.info(self.request, "User updated")
        return super().form_valid(form)


class Delete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "registration/delete.html"
    success_url = "/"

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.warning(self.request, "User deleted")
        return super().form_valid(form)


class GameView(LoginRequiredMixin, FormView):
    form_class = GameForm
    template_name = "main/games.html"
    success_url = "/client/game/"


    def form_valid(self, form: GameForm) -> HttpResponse:
        # commit=False створює object у пам’яті, але НЕ save в DB
        game = form.save(commit=False)
        game.user = self.request.user  #для того щоб вручну не вибирати зі списку users
        game.save()
        messages.success(self.request, "Game created successfully")
        return super().form_valid(form)


class GetGameList(LoginRequiredMixin, ListView):
    template_name = "main/get_gamelist.html"
    paginate_by = 10

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user).order_by("-id")


class GetGame(LoginRequiredMixin, DetailView):
    model = Game
    template_name = "main/get_game.html"
    context_object_name = "game"
    pk_url_kwarg = "game_id"

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)


class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = "main/games.html"
    success_url = "/client/game/"
    pk_url_kwarg = "game_id"

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.info(self.request, "Game updated")
        return super().form_valid(form)


class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = "main/delete-game.html"
    success_url = "/client/game/"
    pk_url_kwarg = "game_id"

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.warning(self.request, "Game deleted")
        return super().form_valid(form)


#@login_required
# def get_game(request, game_id):
#     game = Game.objects.get(pk=game_id, user=request.user)
#     return render(request, template_name="get_game.html", context={"game": game})