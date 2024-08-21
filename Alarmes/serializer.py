from rest_framework import serializers
from Alarmes.models import Allevent


class Alarme_serializer(serializers.ModelSerializer):
    """Lista Alarmes"""
    class Meta:
        model = Allevent
        fields = ['machineid', 'eventid', 'eventtype', 'sourceid', 'servername',
                  'tickstimestamp', 'eventtimestamp', 'eventcategory', 'severity', 'priority', 'message',
                  'conditionname', 'subconditionname', 'alarmclass', 'active', 'acked', 'effdisabled', 'disabled',
                  'effsuppressed', 'suppressed', 'personid', 'changemask', 'inputvalue', 'limitvalue', 'quality',
                  'usercomment', 'computerid', 'tag1value', 'tag2value', 'tag3value', 'tag4value', 'shelved',
                  'autounshelvetime', 'grouppath', 'datetime', 'eventassociationid']


class Alarmes_Create_Serializer(serializers.ModelSerializer):
    """Lista de Criar Alarmes"""

    class Meta:
        model = Allevent
        fields = '__all__'
