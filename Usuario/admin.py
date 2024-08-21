from django.contrib import admin
from .models import AuthUserGroups, AuthGroup, AuthGroupPermissions, TableLog, ControlApi

# Registrar os modelos no admin
admin.site.register(AuthUserGroups)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(TableLog)
admin.site.register(ControlApi)
