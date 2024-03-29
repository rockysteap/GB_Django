from django.urls import path

from s4_app1_game_app.views import games

urlpatterns = [
    path('games/', games, name='games'),
]
