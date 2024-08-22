from rest_framework import serializers
from Receitas.models import DbRecipe, DbRecipe_data


# Update / Lista / CREATE
class Recipe_Serializer(serializers.ModelSerializer):
    """Lista da Nova Receita"""
    class Meta:
        model = DbRecipe
        fields = '__all__'


# Delete
class Receita_Delete_Serializer(serializers.ModelSerializer):
    """Delete dados de Receita"""

    class Meta:
        model = DbRecipe
        fields = ['reg_ativo']


class Recipe_Data_Serializer(serializers.ModelSerializer):
    """Lista de dados da Nova Receita"""
    class Meta:
        model = DbRecipe_data
        fields = '__all__'

