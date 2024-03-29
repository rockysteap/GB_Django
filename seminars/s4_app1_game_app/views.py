import logging

from django.shortcuts import render

from s4_app1_game_app.forms import GamesMenu, GAME_TITLES
from s4_app1_game_app.logic.games import get_results

logger = logging.getLogger(__name__)


def games(request):
    context = {}
    if request.method == 'POST':
        form = GamesMenu(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            tries = form.cleaned_data['tries']
            context['title'] = GAME_TITLES[game]
            context['results'] = get_results(game, tries)
    form = GamesMenu()
    context['form'] = form
    return render(request, 's4_app1_game_app/games.html', context)
