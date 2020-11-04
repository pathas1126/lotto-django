from typing import List
from lotto.utils.lotto_game.lotto_game_generator import LottoGameGenerator


class LottoGame:
    def __init__(self, string_or_length: List[int] or str):
        lotto_game_generator = LottoGameGenerator()
        if type(string_or_length) is str:
            self.lotto_game = lotto_game_generator.create_game_from_string(string_or_length)
        else:
            self.lotto_game = lotto_game_generator.create_game(string_or_length)
            