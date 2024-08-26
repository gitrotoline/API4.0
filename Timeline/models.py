from django.db import models


class DbTimeline(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    ciclo = models.IntegerField(db_column='ciclo', blank=False, null=False)
    evento = models.CharField(max_length=45, db_column='evento', blank=False, null=False)
    datetime = models.DateTimeField(db_column='datetime', blank=False, null=False)
    carro = models.CharField(max_length=2, db_column='carro', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'db_timeline'
        unique_together = ('ciclo', 'evento', 'datetime')


class DbTimelineDados(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    ciclo = models.IntegerField(db_column='ciclo')
    chave = models.CharField(max_length=45)
    valor = models.CharField(max_length=200)
    datetime = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'db_timeline_dados'
        unique_together = ('ciclo', 'chave')


class DbTimeline_sensores(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    ciclo = models.IntegerField(db_column='ciclo', blank=False, null=False)
    evento = models.CharField(max_length=45, db_column='evento', blank=False, null=False)
    datetime = models.DateTimeField(db_column='datetime', blank=False, null=False)
    carro = models.CharField(max_length=2, db_column='carro', blank=False, null=False)
    status = models.BooleanField(db_column='status', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'db_timeline_sensores'
        unique_together = ('ciclo', 'evento', 'datetime', 'carro', 'status')
