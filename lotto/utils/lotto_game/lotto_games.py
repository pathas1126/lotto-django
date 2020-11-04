from lotto.utils.lotto_game.lotto_game_constant import LOTTO_GAMES_LENGTH, LOTTO_GAME_LENGTH
from lotto.utils.lotto_game.lotto_game import LottoGame


class LottoGames:
    def __init__(self, lotto_games_length:int):
        games = []

        count = 0
        while count < LOTTO_GAMES_LENGTH:
            games.append(LottoGame(LOTTO_GAME_LENGTH).lotto_game)
            count += 1
            
        self.lotto_games = games;
    
