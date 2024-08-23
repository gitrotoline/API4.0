from django.contrib.auth.models import User, Group, Permission
from django.db import models
from datetime import datetime


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
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, unique=True, null=False)
    group = models.OneToOneField(Group, on_delete=models.DO_NOTHING, null=False)
    reg_ativo = models.BooleanField(default=1)

    class Meta:
        db_table = 'control_api'


class Empresas_API(models.Model):
    nome = models.CharField(max_length=150, null=False, help_text="Nome da Empresa")
    status = models.BooleanField(default=True, help_text="Status da Empresa")

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "Empresas_API"
        unique_together = ['nome']


class Machines_API(models.Model):
    n_serie = models.CharField(max_length=10, null=False, help_text="Número de série da máquina (M00...)")
    carros = models.IntegerField(null=False, default=0, help_text="Quantidade de carros")
    modelo = models.CharField(max_length=5, help_text="Siga a nomenclatura CR, DC, SO...")
    empresa = models.ForeignKey(Empresas_API, on_delete=models.CASCADE, null=False, help_text="Empresa dona da máquina")
    data_active = models.DateTimeField(null=False, help_text="Data de ativação da API", default=datetime.now())
    status = models.BooleanField(default=1, help_text="Status da API dessa máquina")

    def __str__(self):
        return f"{self.n_serie} -  {self.empresa}"

    class Meta:
        db_table = "Machine_com_API"
        unique_together = ["n_serie"]


class User_Acess_Machines(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    machine = models.ForeignKey(Machines_API, on_delete=models.CASCADE, null=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} tem acesso a {self.machine} - Status = {self.status}"

    class Meta:
        db_table = "Usuarios_e_Machines_Access_API"
        unique_together = ['user', 'machine']


class Token_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    token = models.CharField(max_length=500, null=False)

    class Meta:
        db_table = "Token_user"
        unique_together = ['user', "token"]

