from rest_framework import serializers
from Horimetros.models import DbHorimeter


class Horimeter_Serializer(serializers.ModelSerializer):
    """Lista dados de Horimetros"""
    class Meta:
        model = DbHorimeter
        fields = '__all__'
