from typing import List
from lotto.utils.lotto_game.lotto_game_constant import LOTTO_GAME_LENGTH, LOTTO_GAME_WITH_BONUS_LENGTH, LOTTO_NUMBERS_LENGTH
from lotto.exceptions import InvalidLottoGame
from lotto.utils.lotto_game.lotto_numbers import LottoNumbers
import random

class LottoGameGenerator:
   

    def create_random_index(self, max:int):
        """
        Create Random Index by Max
        """
        return random.randint(0, max - 1)

    def shuffle_numbers(self, lotto_numbers: List[int], shuffle_times:int):
        """
        Shuffle Lotto Numbers
        """
        count = 0
        while count < shuffle_times:
    
            size_before_remove = len(lotto_numbers)
            remove_target_index = self.create_random_index(size_before_remove)
            
            popped_number = lotto_numbers.pop(remove_target_index)

            size_after_remove = len(lotto_numbers)
            add_target_index = self.create_random_index(size_after_remove)

            lotto_numbers.insert(add_target_index, popped_number)
            
            count += 1
        return lotto_numbers;
    
    def create_game(self, game_length:int):
        """
        Create Lotto Game
        """
        game = []
        lotto_numbers = LottoNumbers(LOTTO_NUMBERS_LENGTH).lotto_numbers

        shuffle_times = 30
        count = 0

        while count < game_length:
            game.append((self.shuffle_numbers(lotto_numbers, shuffle_times)).pop())
            count += 1

        if self.verify_valid_game(game):
            return game

    def create_game_from_string(self, numbers_string:str):
        """
        Create Lotto Game from String
        """
        game = []
        number_chars = numbers_string.split()
        for char in number_chars:
            game.append(int(char))

        if self.verify_valid_game(game):
            return game

    def verify_valid_game(self, lotto_game:List[int]):
        """
        Verify Lotto Game is Valid
        """
        is_valid = True;
        lotto_game_temp = []
        for number in lotto_game:
            if number not in lotto_game_temp:
                lotto_game_temp.append(number)
            else:
                print(number, lotto_game, lotto_game_temp)
                is_valid = False
                raise InvalidLottoGame
                
        lotto_game_temp_length = len(lotto_game_temp)
        if lotto_game_temp_length != LOTTO_GAME_LENGTH and lotto_game_temp_length != LOTTO_GAME_WITH_BONUS_LENGTH:
            print(lotto_game_temp)
            is_valid = False
            raise InvalidLottoGame

        return is_valid

    