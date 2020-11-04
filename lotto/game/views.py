from lotto.utils.lotto_game.lotto_game_constant import LOTTO_GAMES_LENGTH, LOTTO_GAME_LENGTH
from lotto.exceptions import LottoGameSaveFail
from lotto.game.serializers import LottoGameSerializer
from lotto.models import Lotto
from lotto.utils.lotto_game.lotto_game import LottoGame
from lotto.utils.lotto_game.lotto_games import LottoGames
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def response_success(response_data):
    return Response(data={'result': {'data':response_data, 'status':"SUCCESS", 'message': "hello"}}, status=status.HTTP_200_OK)

class LottoWinningGameView(APIView):

    serializer_class = LottoGameSerializer

    def get(self, request):
        first = Lotto.objects.first()
        numbers = LottoGameSerializer(first).data['numbers']

        lotto_game = LottoGame(numbers).lotto_game

        response_data = {"winningGame": lotto_game}
        
        return response_success(response_data)

class LottoRandomGameView(APIView):

    def get(self, request):
        lotto_game = LottoGame(LOTTO_GAME_LENGTH).lotto_game

        response_data = {"randomGame": lotto_game}

        return response_success(response_data)

class CreateCustomLottoGame(APIView):
    
    serializer_class = LottoGameSerializer

    def post(self, request):
        custom_game = request.data['customGame']
        string_custom_game = ""
        for number in custom_game:
            if len(string_custom_game) is 0:
                string_custom_game += str(number)
            else:
                string_custom_game += " " + str(number)

        try:
            lotto_game_saved = Lotto.objects.create(numbers=string_custom_game)
            lotto_game_saved_serialized = LottoGameSerializer(lotto_game_saved).data['numbers']
            lotto_game = LottoGame(lotto_game_saved_serialized).lotto_game
            
            response_data = {"customGame": lotto_game}

            return response_success(response_data)
        except:
            raise LottoGameSaveFail

class LottoRandomGamesView(APIView):

    def get(self, request):
        lotto_games = LottoGames(LOTTO_GAMES_LENGTH).lotto_games

        response_data = {"randomGames": lotto_games}

        return response_success(response_data)
