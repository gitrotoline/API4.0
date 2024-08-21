from datetime import timezone, datetime
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import Group, Permission, User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from Usuario.fux_auxiliares import enviarCredentials
from Usuario.models import TableLog, AuthGroupPermissions


def emailUser(request):
    return render(request, 'emailUser.html')


def usuario_auto(request):
    # Verifica se o email foi informado
    if len(request.POST['email']) == 0:
        messages.warning(request, "Por Favor, Informe um email válido!")
        return HttpResponseRedirect(reverse("auto_usuarios"))

    # Cria o usuário Admin, se não existir
    if not User.objects.filter(username='Admin').exists():
        try:
            admin_user = User.objects.create_superuser('Admin', 'ti@rotoline.com', 'r0t0line!@#$')
            admin_user.last_login = timezone.now()  # Define o campo last_login com o timestamp atual
            admin_user.save()
        except Exception as e:
            print(e)

    # Envia as credenciais por email
    enviarCredentials(request)

    # Cria ou atualiza os usuários Supervisor e Operador

    user, created = User.objects.get_or_create(username="Supervisor", defaults={'email': 'ti@rotoline.com'})
    if created:
        user.set_password('r0t0line!@#$')  # Define uma senha padrão

    user.last_login = timezone.now()  # Define o campo last_login com o timestamp atual
    user.save()

    # Registra o termo de privacidade no log
    logTerms = TableLog(termsOfPrivacy=0, userId=user.id)
    logTerms.save()

    # Cria o grupo Api, se não existir
    if not Group.objects.filter(name='Api').exists():
        print("aqui")
        groupApi = Group(name='Api')
        groupApi.save()
    else:
        groupApi = Group.objects.get(name='Api')

    # Adiciona permissões ao grupo Api
    permissoes = Permission.objects.all()
    listPermissions = [29, 30, 61, 140, 141, 142, 178, 194, 195, 196, 197, 198]
    try:
        for p in permissoes:
            if p.id in listPermissions or 40 <= p.id <= 57 or 65 <= p.id <= 85 or 97 <= p.id <= 137 or 183 <= p.id <= 190 or 222 <= p.id <= 235:
                groupPermissions = AuthGroupPermissions(group_id=groupApi.id, permission_id=p.id)
                groupPermissions.save()
        print("terminei o for")

    except IntegrityError:
        messages.warning(request, _("As configurações padrão já constam no Banco de Dados"))
        return HttpResponseRedirect(reverse('home2'))

    return HttpResponse(_('Usuários já existem no Banco de Dados'))
