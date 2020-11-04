from rest_framework import exceptions, status

class InvalidLottoGame(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        'success': "FAIL",
        'message': "잘못된 로또 번호입니다."
    }

class LottoGameSaveFail(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail ={
        'success': "FAIL",
        'message': "로또 번호 저장에 실패했습니다."
    }