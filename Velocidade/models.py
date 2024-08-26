from django.db import models


class Speed(models.Model):
    cycle = models.IntegerField(null=False, blank=False, help_text="Id of cycle")
    type = models.CharField(max_length=50, null=False, blank=False, help_text="type of sensor")
    cart = models.CharField(null=False, blank=False, help_text="Cart of machine")
    sensor = models.CharField(null=False, blank=False, help_text="sensor of part the cart (Arm, Plate or Cart)")
    value_hz = models.FloatField(null=False, blank=False, help_text="Value in Hertz unit")
    value_rpm = models.FloatField(null=False, blank=False, help_text="Value in RPM unit (Rotation per Minutes")
    datetime = models.DateTimeField(null=False, blank=False, help_text="Datetime of event")

    class Meta:
        db_table = 'db_speed'
        unique_together = ("cycle", "cart", "sensor", "datetime")
