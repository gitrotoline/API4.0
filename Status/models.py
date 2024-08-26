from django.db import models


class Status_Machine(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    timezone = models.CharField(null=True, max_length=80)

    class Meta:
        db_table = 'db_status_machine'