from lotto.utils.lotto_game.lotto_game_constant import LOTTO_NUMBERS_LENGTH


class LottoNumbers:
    def __init__(self, lotto_numbers_length:int):
        self.lotto_numbers = self.create_lotto_numbers(LOTTO_NUMBERS_LENGTH)

    def create_lotto_numbers(self, numbers_length:int):
        """
        Create Lotto Numbers by Numbers Length
        """
        lotto_numbers = list(range(1, numbers_length))
        return lotto_numbers    
