from django.db import models
from .manager import AlleventManager


class Allevent(models.Model):
    eventid = models.CharField(db_column='EventID', max_length=36, primary_key=True)  # Field name made lowercase.
    machineid = models.CharField(db_column='MachineID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    eventtype = models.IntegerField(db_column='EventType', blank=True, null=True)  # Field name made lowercase.
    sourcename = models.CharField(db_column='SourceName', max_length=200, blank=True,null=True)  # Field name made lowercase.
    sourcepath = models.CharField(db_column='SourcePath', max_length=512, blank=True,null=True)  # Field name made lowercase.
    sourceid = models.CharField(db_column='SourceID', max_length=36, blank=True,null=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tickstimestamp = models.BigIntegerField(db_column='TicksTimeStamp', blank=True,null=True)  # Field name made lowercase.
    eventtimestamp = models.DateTimeField(db_column='EventTimeStamp', blank=True,null=True)  # Field name made lowercase.
    eventcategory = models.CharField(db_column='EventCategory', max_length=50, blank=True,null=True)  # Field name made lowercase.
    severity = models.IntegerField(db_column='Severity', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=512, blank=True, null=True)  # Field name made lowercase.
    conditionname = models.CharField(db_column='ConditionName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subconditionname = models.CharField(db_column='SubConditionName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alarmclass = models.CharField(db_column='AlarmClass', max_length=40, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=50, blank=True, null=True)  # Field name made lowercase.
    acked = models.IntegerField(db_column='Acked', blank=True, null=True)  # Field name made lowercase.
    effdisabled = models.IntegerField(db_column='EffDisabled', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='Disabled', blank=True, null=True)  # Field name made lowercase.
    effsuppressed = models.IntegerField(db_column='EffSuppressed', blank=True, null=True)  # Field name made lowercase.
    suppressed = models.CharField(db_column='Suppressed', max_length=6, blank=True, null=True)  # Field name made lowercase.
    personid = models.CharField(db_column='PersonID', max_length=50, blank=True,null=True)  # Field name made lowercase.
    changemask = models.IntegerField(db_column='ChangeMask', blank=True, null=True)  # Field name made lowercase.
    inputvalue = models.FloatField(db_column='InputValue', blank=True, null=True)  # Field name made lowercase.
    limitvalue = models.FloatField(db_column='LimitValue', blank=True, null=True)  # Field name made lowercase.
    quality = models.IntegerField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.
    eventassociationid = models.CharField(db_column='EventAssociationID', max_length=36, blank=True,  null=True)  # Field name made lowercase.
    usercomment = models.CharField(db_column='UserComment', max_length=512, blank=True, null=True)  # Field name made lowercase.
    computerid = models.CharField(db_column='ComputerID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    tag1value = models.CharField(db_column='Tag1Value', max_length=128, blank=True,  null=True)  # Field name made lowercase.
    tag2value = models.CharField(db_column='Tag2Value', max_length=128, blank=True,null=True)  # Field name made lowercase.
    tag3value = models.CharField(db_column='Tag3Value', max_length=128, blank=True, null=True)  # Field name made lowercase.
    tag4value = models.CharField(db_column='Tag4Value', max_length=128, blank=True, null=True)  # Field name made lowercase.
    shelved = models.CharField(db_column='Shelved', max_length=6, blank=True, null=True)  # Field name made lowercase.
    autounshelvetime = models.DateTimeField(db_column='AutoUnshelveTime', blank=True,  null=True)  # Field name made lowercase.
    grouppath = models.CharField(db_column='GroupPath', max_length=254, blank=True,null=True)  # Field name made lowercase.
    messageid = models.CharField(db_column='MessageID', max_length=254, blank=True, null=True)
    datetime = models.DateTimeField(db_column='datetime', null=False)
    # createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    # updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    objects = AlleventManager() #ativa o manager do tabela

    class Meta:
        managed = True #nao permite o django editar a tabela
        db_table = 'events' #nome da tabela existente no banco
        permissions = (
            ('dashboard', 'User pode visualizar dashboard'),
            ('api_alarmes', 'User pode visualizar api_turno'),
        )# Permissões da classe Allevent