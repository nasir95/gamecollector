from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Game, Console


# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})


def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    consoles_game_doesnt_have = Console.objects.exclude(
        id__in=game.consoles.all().values_list('id'))
    return render(request, 'games/detail.html', {'game': game, 'consoles': consoles_game_doesnt_have})


def assoc_console(request, game_id, console_id):
    Game.objects.get(id=game_id).consoles.add(console_id)
    return redirect('detail', game_id=game_id)


def remove_assoc_console(request, game_id, console_id):
    Game.objects.get(id=game_id).consoles.remove(console_id)
    return redirect('detail', game_id=game_id)


class GameCreate(CreateView):
    model = Game
    fields = ['name', 'genre', 'rating', 'description', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'


class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'


class ConsoleList(ListView):
    model = Console


class ConsoleDetail(DetailView):
    model = Console


class ConsoleCreate(CreateView):
    model = Console
    fields = ['name', 'color']
    success_url = '/consoles/'


class ConsoleUpdate(UpdateView):
    model = Console
    fields = ['name', 'color']
    success_url = '/consoles/'


class ConsoleDelete(DeleteView):
    model = Console
    success_url = '/consoles/'
