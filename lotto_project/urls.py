"""lotto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from lotto.game.views import CreateCustomLottoGame, LottoRandomGameView, LottoRandomGamesView, LottoWinningGameView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

lotto_game_patterns = [
    path('winning', LottoWinningGameView.as_view()),
    path('random', LottoRandomGameView.as_view()),
    path('custom', CreateCustomLottoGame.as_view())
]

lotto_games_patterns = [
    path('random', LottoRandomGamesView.as_view())
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('lotto/game/', include(lotto_game_patterns)),
        path('lotto/games/', include(lotto_games_patterns)),
    ]))
]
