from django.db import models
from .manager import RelatorioresumidoManager


# Create your models here.
class Relatorioresumido(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='datetime', blank=True, null=True)  # Field name made lowercase.
    carro = models.CharField(db_column='Carro', max_length=2, blank=True, null=True)  # Field name made lowercase.
    receita = models.CharField(db_column='Receita', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datainicio = models.CharField(db_column='DataInicio', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    inicioforno = models.CharField(db_column='InicioForno', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    fimforno = models.CharField(db_column='FimForno', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    duracaoforno = models.CharField(db_column='DuracaoForno', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    sp_temperatura = models.FloatField(db_column='SP_Temperatura', blank=True, null=True)  # Field name made lowercase.
    fimciclo = models.CharField(db_column='FimCiclo', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    duracaociclo = models.CharField(db_column='DuracaoCiclo', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    cozidos = models.CharField(db_column='Cozidos', max_length=50, blank=True, null=True)  # Field name made lowercase.
    duracaoparada = models.CharField(db_column='DuracaoParada', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    gas = models.FloatField(db_column='Gas', blank=True, null=True)  # Field name made lowercase.
    energia = models.FloatField(db_column='Energia', blank=True, null=True)  # Field name made lowercase.
    indice = models.IntegerField(db_column='Indice', blank=True, null=True)  # Field name made lowercase.
    id_conjunto = models.IntegerField(blank=True, null=True)
    id_receita = models.IntegerField(blank=True, null=True)

    objects = RelatorioresumidoManager()

    class Meta:
        managed = True
        db_table = 'db_producao'