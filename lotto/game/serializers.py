from lotto.models import Lotto
from rest_framework import serializers


class LottoGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lotto
        fields = '__all__'
