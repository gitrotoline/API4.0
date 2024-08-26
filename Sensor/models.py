from django.db import models


class Sensor(models.Model):
    sensor = models.CharField(max_length=50)
    datetime = models.DateTimeField(max_length=8)
    carro = models.CharField(max_length=2)
    valor = models.FloatField()
    medida = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'db_sensor'
        unique_together = ('sensor', 'datetime', 'carro')
