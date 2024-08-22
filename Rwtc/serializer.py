from rest_framework import serializers

from Rwtc.models import RWTC


class RWTC_serializer(serializers.ModelSerializer):
    class Meta:
        model = RWTC
        fields = '__all__'