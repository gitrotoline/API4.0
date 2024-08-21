from django.db import models
from django.db.models import Count
from datetime import date

class RelatorioresumidoManager(models.Manager):

    ######################################################## SQL SERVER ##########################################################################################
    def ciclos_dia_SQL(self): #retorna os ciclos por dia com a data convertida para date
        return self.extra({'data': "CONVERT(Date, datetime,103)"}).values('data').annotate(ciclos=Count('id')).order_by('data')

    def ciclos_now_SQL(self): #retorna a quantidade de ciclo realizados no dia atual
        return self.extra({'data': "CONVERT(Date, datetime,103)"}).values('data').annotate(ciclos=Count('id')).order_by('data').filter(datetime__date=(date.today()))

    def ciclos_turnos_SQL(self): #retorna os ciclos sem ordernar
        return self.extra({'data': "CONVERT(Date, datetime,103)"}).values('data').annotate(ciclos=Count('id'))

    def ciclos_carros_SQL(self): #retorna os ciclos realizados por dia de cada carro
        return self.extra({'data': "CONVERT(Date, datetime,103)"}).values('data', 'carro').annotate(ciclos=Count('id'))

    def data_ultimo_ciclo_SQL(self): #retorna a data do ultimo ciclo realizado
        return self.ciclos_dia().last().get('data')

    def ciclos_mes_ano_SQL(self): # retorna os ciclos contados por mes e ano
        return self.extra({'ano': "YEAR(CONVERT(Date, datetime,103))", 'mes': "MONTH(CONVERT(Date, datetime,103))"}).values('ano', 'mes').annotate(ciclos=Count('id'))

    def ciclos_dia_turnos_SQL(self, inicio, fim): # retorna os ciclos filtrados pelo horario
        return self.extra({'data': "CONVERT(Date, datetime,103)"}).values('data').annotate(ciclos=Count('id')).order_by('data').filter(datetime__time__range=(inicio, fim))

    def tempos_trabalho_SQL(self): # retorna a soma da duração de ciclo e duração de parada do dia, quando a duração de parada for menor que 3 horas
        return self.extra({'data': "CONVERT(Date, datetime,103)"}).values('duracaociclo', 'data','duracaoparada').filter(duracaoparada__lte='03:00:00').order_by('data')


    def ciclos_carro_geral_SQL(self): # retorna a quantidade de ciclos realizada por cada carro Total
        return self.values('carro').annotate(ciclos=Count('id'))

######################################################## MYSQL ##########################################################################################

    def ciclos_dia(self): #retorna os ciclos por dia com a data convertida para date
        #return self.extra({'data': "CONVERT(Date, dateandtime,103)"}).values('data').annotate(ciclos=Count('id')).order_by('data')
        return self.extra({'data': "CONVERT(datetime,DATE)"}).values('data').annotate(ciclos=Count('id')).order_by('data')

    def ciclos_now(self): #retorna a quantidade de ciclo realizados no dia atual
        #return self.extra({'data': "CONVERT(Date, dateandtime,103)"}).values('data').annotate(ciclos=Count('id')).order_by('data').filter(dateandtime__date=(date.today()))
        return self.extra({'data': "CONVERT(datetime,DATE)"}).values('data').annotate(ciclos=Count('id')).order_by('data').filter(datetime__date=(date.today()))

    def ciclos_turnos(self): #retorna os ciclos sem ordernar
        #return self.extra({'data': "CONVERT(Date, dateandtime,103)"}).values('data').annotate(ciclos=Count('id'))
        return self.extra({'data': "CONVERT(datetime,DATE)"}).values('data').annotate(ciclos=Count('id'))

    def ciclos_carros(self): #retorna os ciclos realizados por dia de cada carro
        #return self.extra({'data': "CONVERT(Date, dateandtime,103)"}).values('data', 'carro').annotate(ciclos=Count('id'))
        return self.extra({'data': "CONVERT(datetime,DATE)"}).values('data', 'carro').annotate(ciclos=Count('id'))

    def data_ultimo_ciclo(self): #retorna a data do ultimo ciclo realizado
        #return self.ciclos_dia().last().get('data')
        return self.ciclos_dia().last().get('data')

    def ciclos_mes_ano(self): # retorna os ciclos contados por mes e ano
        #return self.extra({'ano': "YEAR(CONVERT(Date, dateandtime,103))", 'mes': "MONTH(CONVERT(Date, dateandtime,103))"}).values('ano', 'mes').annotate(ciclos=Count('id'))
        return self.extra({'ano': "YEAR(CONVERT(datetime,DATE))", 'mes': "MONTH(CONVERT(datetime,DATE))"}).values('ano', 'mes').annotate(ciclos=Count('id'))

    def ciclos_dia_turnos(self, inicio, fim): # retorna os ciclos filtrados pelo horario
        #return self.extra({'data': "CONVERT(Date, dateandtime,103)"}).values('data').annotate(ciclos=Count('id')).order_by('data').filter(dateandtime__time__range=(inicio, fim))
        return self.extra({'data': "CONVERT(datetime,DATE)"}).values('data').annotate(ciclos=Count('id')).order_by('data').filter(datetime__time__range=(inicio, fim))

    def tempos_trabalho(self): # retorna a soma da duração de ciclo e duração de parada do dia, quando a duração de parada for menor que 3 horas
        #return self.extra({'data': "CONVERT(Date, dateandtime,103)"}).values('duracaociclo', 'data','duracaoparada').filter(duracaoparada__lte='03:00:00').order_by('data')
        return self.extra({'data': "CONVERT(datetime,DATE)"}).values('duracaociclo', 'data','duracaoparada').filter(duracaoparada__lte='03:00:00').order_by('data')

    def ciclos_carro_geral(self): # retorna a quantidade de ciclos realizada por cada carro Total
        #return self.values('carro').annotate(ciclos=Count('id'))
        return self.values('carro').annotate(ciclos=Count('id'))