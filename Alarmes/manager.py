from django.db import models
from django.db.models import Count


class AlleventManager(models.Manager):
    def alarmes_dia_SQL(self): #retorna a quantidade de alarmes ativos, excluindo "Alarm fault"  e converte a data do banco de datetime para date
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'data': "CONVERT(Date, eventtimestamp,103)"}).values('data').annotate(
            alarmes=Count('eventid'))

    def alarmes_mes_ano_SQL(self): #retorna a quantidade de alarmes gerada por mes e ano da maquina  - alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'ano': "YEAR(CONVERT(Date, eventtimestamp,103))", 'mes':
            "MONTH(CONVERT(Date,eventtimestamp,103))"}).values('ano', 'mes').annotate(alarmes=Count('eventid'))

    # NAO USA MAIS, SUBSTITUDO POR alarmes_utc
    def alarmes_dia_turno_SQL(self, inicio, fim): #retorna a quantidade de alarmes gerada por dia com range de horario - alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).extra({'data': "CONVERT(Date, eventtimestamp,103)", 'even':"DATEADD(mi, DATEDIFF(mi, GETUTCDATE(), GETDATE()), Eventtimestamp)"}).values('data').annotate(alarmes=Count('eventid')).filter(eventtimestamp__time__range=(inicio, fim)).order_by('-data')

    def alarmes_ocorrencia_SQL(self): #retorna a quantidade de vezes que ocorreu cada alarme (message) -alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).extra({'data': "CONVERT(Date, eventtimestamp,103)"}).values('data','message').annotate(ocorrencia=Count('message')).exclude(message__contains='Alarm fault').order_by('-ocorrencia')

    def alarmes_ocorrencia_turno_SQL(self, inicio, fim): #retorna a quantidade de vezes que ocorreu cada alarme (message) filtrado pelo horario -alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).extra({'data': "CONVERT(Date, eventtimestamp,103)"}).filter(
            eventtimestamp__time__range=(inicio, fim)).values('data', 'message').annotate(ocorrencia=Count('message')). \
            exclude(message__contains='Alarm fault').order_by('-ocorrencia')

    def alarmes_top_SQL(self): #retorna os alarmes que mais aconteceram  -alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'data': "CONVERT(Date, eventtimestamp,103)"}).values('message').annotate(alarmes=Count('eventid')).order_by('-alarmes')

    def alarmes_utc_SQL(self):
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'data': "CONVERT(Date, eventtimestamp,103)", 'even':"DATEADD(mi, DATEDIFF(mi, GETUTCDATE(), GETDATE()), Eventtimestamp)"}).values('even', 'data')

    def alarmes_message_utc_SQL(self):  # retorna a quantidade de vezes que ocorreu cada alarme (message) filtrado pelo horario -alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'data': "CONVERT(Date, eventtimestamp,103)", 'even':"DATEADD(mi, DATEDIFF(mi, GETUTCDATE(), GETDATE()), Eventtimestamp)"}).values('data','even', 'message')



########################################################## _MYSQL_ ##############################################################
    def alarmes_dia(self): #retorna a quantidade de alarmes ativos, excluindo "Alarm fault"  e converte a data do banco de datetime para date
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'data': "CONVERT(eventtimestamp,DATE)"}).values('data').annotate(alarmes=Count('eventid'))

    def alarmes_mes_ano(self): #retorna a quantidade de alarmes gerada por mes e ano da maquina  - alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'ano': "YEAR(CONVERT(eventtimestamp,DATE))", 'mes':
            "MONTH(CONVERT(eventtimestamp,DATE))"}).values('ano', 'mes').annotate(alarmes=Count('eventid'))

    # NAO USA MAIS, SUBSTITUDO POR alarmes_utc
    def alarmes_dia_turno(self, inicio, fim): #retorna a quantidade de alarmes gerada por dia com range de horario - alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).extra({'data': "CONVERT(eventtimestamp,DATE)", 'even':"DATE_ADD(Eventtimestamp, INTERVAL DATEDIFF(UTC_TIMESTAMP(), now()) HOUR)"}).values('data').annotate(alarmes=Count('eventid')).filter(eventtimestamp__time__range=(inicio, fim)).order_by('-data')

    def alarmes_ocorrencia(self): #retorna a quantidade de vezes que ocorreu cada alarme (message) -alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).extra({'data': "CONVERT(eventtimestamp,DATE)"}).values('data','message').annotate(ocorrencia=Count('message')).exclude(message__contains='Alarm fault').order_by('-ocorrencia')

    def alarmes_ocorrencia_turno(self, inicio, fim): #retorna a quantidade de vezes que ocorreu cada alarme (message) filtrado pelo horario -alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).extra({'data': "CONVERT(eventtimestamp,DATE)"}).filter(
            eventtimestamp__time__range=(inicio, fim)).values('data', 'message').annotate(ocorrencia=Count('message')). \
            exclude(message__contains='Alarm fault').order_by('-ocorrencia')

    def alarmes_top(self): #retorna os alarmes que mais aconteceram  -alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'data': "CONVERT(eventtimestamp,DATE)"}).values('message').annotate(alarmes=Count('eventid')).order_by('-alarmes')

    def alarmes_utc(self):
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'data': "CONVERT(eventtimestamp,DATE)", 'even':"DATE_ADD(Eventtimestamp, INTERVAL DATEDIFF(UTC_TIMESTAMP(), now()) HOUR)"}).values('even', 'data')

    def alarmes_message_utc(self):  # retorna a quantidade de vezes que ocorreu cada alarme (message) filtrado pelo horario -alarmes ativos, excluindo "Alarm fault"
        return self.filter(active=1).exclude(message__contains='Alarm fault').extra({'data': "CONVERT(eventtimestamp,DATE)", 'even':"DATE_ADD(Eventtimestamp, INTERVAL DATEDIFF(UTC_TIMESTAMP(), now()) HOUR)"}).values('data','even', 'message')

