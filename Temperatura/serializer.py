from rest_framework import serializers
from Temperatura.models import DbTemperature


class Temperature_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DbTemperature
        fields = '__all__'