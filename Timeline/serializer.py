from rest_framework import serializers
from Timeline.models import DbTimeline, DbTimelineDados, DbTimeline_sensores


# Timeline Edi (Supervisorio) ---------------------------------------------
class TimeLine_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DbTimeline
        fields = '__all__'


class TimeLine_Dados_Serializer(serializers.ModelSerializer):

    class Meta:
        model = DbTimelineDados
        fields = '__all__'

#  ---------------------------------------------------------------------------------------------------------------------


# Timeline Emerson (Direct of PLC) -------------------------------------------------------------------------------------
class TimeLine_CLP_Serializer(serializers.ModelSerializer):
    """Lista dados TimeLine"""

    class Meta:
        model = DbTimeline_sensores
        fields = '__all__'

# ----------------------------------------------------------------------------------------------------------------------