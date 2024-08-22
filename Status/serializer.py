from rest_framework import serializers
from Status.models import Status_Machine


class Status_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Status_Machine
        fields = '__all__'

