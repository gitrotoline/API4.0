from rest_framework import serializers

from Producao.models import Relatorioresumido


class Producao_Serializer(serializers.ModelSerializer):
    """Lista e Edita dados de produção --- Não disponibilizado --- """

    class Meta:
        model = Relatorioresumido
        fields = '__all__'


class Producao_Serializer_GET(serializers.ModelSerializer):
    """Lista e Edita dados de produção --- Não disponibilizado --- """

    class Meta:
        model = Relatorioresumido
        fields = ['id', 'datetime', 'carro', 'receita', 'datainicio', 'inicioforno', 'fimforno', 'duracaoforno',
                  'sp_temperatura', 'fimciclo', 'duracaociclo', 'duracaoparada']
