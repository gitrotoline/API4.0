from rest_framework import serializers

from Sensor.models import Sensor


class Sensor_Serializer(serializers.ModelSerializer):
    """Lista dados Sensor"""

    class Meta:
        model = Sensor
        fields = '__all__'


class Sensor_Serializer_GET(serializers.ModelSerializer):
    """Lista dados Sensor"""

    class Meta:
        model = Sensor
        fields = ['sensor', 'valor', 'medida', 'datetime']