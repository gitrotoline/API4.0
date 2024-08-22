from rest_framework import serializers
from Corrente.models import Corrente_Eletrica


class Corrente_Eletrica_serializer(serializers.ModelSerializer):
    class Meta:
        model = Corrente_Eletrica
        fields = '__all__'
