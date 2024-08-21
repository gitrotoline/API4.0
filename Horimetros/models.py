from django.db import models


class DbHorimeter(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    machineID = models.CharField(null=False, max_length=5)
    datetime = models.DateTimeField(null=False, blank=False)
    nome = models.CharField(max_length=50, null=False)
    valor = models.IntegerField(null=False)

    class Meta:
        managed = True
        db_table = 'db_horimeter'
        unique_together = ('machineID', 'nome')


class DbHorimeter_reset(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    machineID = models.CharField(null=False, max_length=5)
    datetime = models.DateTimeField(null=False, blank=False)
    nome = models.CharField(max_length=50, null=False)
    valor = models.IntegerField(null=False)

    class Meta:
        managed = True
        db_table = 'db_horimeter_reset'