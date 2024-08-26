from django.db import models


class RWTC(models.Model):
    cycle = models.IntegerField(null=False, blank=False, help_text="Id of cycle")
    type = models.CharField(max_length=50, null=False, blank=False, help_text="type of sensor")
    cart = models.CharField(null=False, blank=False, help_text="Cart of machine")
    station = models.CharField(null=False, blank=False, help_text="Station cart in machine")
    value = models.FloatField(null=False, blank=False, help_text="value od event")
    unit = models.CharField(null=False, blank=False, help_text="unit of measurement")
    datetime = models.DateTimeField(null=False, blank=False, help_text="Datetime of event")

    class Meta:
        db_table = "db_rwtc"
        unique_together = ("cycle", "cart", "station", "datetime")
