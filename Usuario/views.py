from datetime import timezone
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import Group, Permission, User
from django.db import IntegrityError, connections
from django.http import HttpResponse, HttpResponseRedirect, Http404
from Usuario.fux_auxiliares import enviarCredentials
from Usuario.models import TableLog, AuthGroupPermissions
import re
from django.db.utils import ConnectionDoesNotExist
from django.utils.translation import get_language
from django.shortcuts import render, reverse


def documentation(request, machine):
    machines = ["M442", "M365", "M453", "M407", "M508", "M537", "M567", "TESTE"]

    # # Verificar se o formato é "M" seguido por 1 a 3 dígitos
    # if not re.match(r'^M\d{1,3}$', machine) or machine != "TESTE":
    #     print("aqui", machine)
    #     raise Http404("Invalid machine format.")

    # Verificar se a máquina está na lista
    if machine not in machines:
        raise Http404("Machine not found.")

    # Passando a linguagem atual para o template
    return render(request, "Documentation/api_documentation/api_documentation.html", {"lang": get_language()})


def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    return render(request, 'errors/500.html', status=500)


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
