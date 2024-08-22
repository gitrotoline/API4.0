from django.contrib.auth.models import User, Group, Permission
from django.db import models


class AuthUserGroups(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey(Permission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class TableLog(models.Model):
    termsOfPrivacy = models.BooleanField(default=0)
    userId = models.IntegerField()

    class Meta:
        db_table = 'table_log'


class ControlApi(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.DO_NOTHING, unique=True, null=False)
    group_user_id = models.OneToOneField(AuthUserGroups, on_delete=models.DO_NOTHING, null=False)
    reg_ativo = models.BooleanField(default=1)

    class Meta:
        db_table = 'control_api'



