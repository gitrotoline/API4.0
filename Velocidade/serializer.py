from rest_framework import serializers

from Velocidade.models import Speed


class Speed_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Speed
        fields = '__all__'
