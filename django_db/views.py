from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView, ListView

from django.contrib.auth import authenticate, login


from .forms import ClientForm, GameForm, UserForm
from .models import Game


class UserView(FormView):
    form_class = UserForm
    template_name = "user.html"
    success_url = "/client/"

    def form_valid(self, form: UserForm) -> HttpResponse:
        form.save()
        user = authenticate(username=form.cleaned_data["username"],
                            password=form.cleaned_data["password1"])
        if user is None:
            return HttpResponse({"error": "Invalid username or password!"})
        else:
            login(self.request, user)

        return super().form_valid(form)


def client_view(request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("game-view")

    return render(request, template_name="main.html", context={"form": form})


class GameView(FormView):
    form_class = GameForm
    template_name = "games.html"
    success_url = "/client/"

    def form_valid(self, form: GameForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class GetGame(ListView):
    template_name = "get_game.html"
    queryset = Game.objects.all()


def get_game(request):
    game = Game.objects.filter(genre__contains="3")
    return HttpResponse(game)
