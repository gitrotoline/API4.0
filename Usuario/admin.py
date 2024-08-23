from django.contrib import admin
from .models import AuthGroup, AuthGroupPermissions, ControlApi, Machines_API, Empresas_API, User_Acess_Machines, \
    Token_user

# Registrar os modelos no admin
admin.site.register(ControlApi)
admin.site.register(Token_user)
admin.site.register(Empresas_API)
admin.site.register(Machines_API)
admin.site.register(User_Acess_Machines)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)

