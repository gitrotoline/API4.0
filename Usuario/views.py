from datetime import timezone
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import Group, Permission, User
from django.db import IntegrityError, connections
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from Usuario.forms import RegisterForm
from Usuario.fux_auxiliares import enviarCredentials, decrypt_name, encrypt_name
from Usuario.models import TableLog, AuthGroupPermissions, Token_user, AuthGroup, ControlApi
from django.utils.translation import get_language
from django.shortcuts import render, reverse, redirect
from Usuario.serializers import CustomTokenObtainSerializer


def index(request):
    dados_machine = []
    return render(request, 'api/page_apresentations_dados_machine.html', {
        'lang': get_language(), 'dados_machines': dados_machine})


# ----------------------------------- DOCUMENTATION API ----------------------------------------------------------------
@login_required()
def documentation(request, machine):
    return render(request, "Documentation/api_documentation/api_documentation.html",
                  {"lang": get_language()})

# --------------------------------------------------------------------------------------------------------------------


# Erros HTTP -----------------------------------------------------------------------------------------------------------
def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    return render(request, 'errors/500.html', status=500)

# ----------------------------------------------------------------------------------------------------------------------


# criar usuarios na primeira instalação --------------------------------------------------------------------------------
def email_user(request):
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
        return HttpResponseRedirect(reverse('home'))

    return HttpResponse(_('Usuários já existem no Banco de Dados'))


# ------------------------------------------ end create user -----------------------------------------------------------


# ------------------------------------------- gera e armazena o token solict via /api_token/ ---------------------------

class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer

# endpoint /api_token/ -------------------------------------------------------------------------------------------------


# ---------------------------------- LOGIN -----------------------------------------------------------------------------

def validate_user(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
        except MultiValueDictKeyError as error:
            messages.error(request, _(f'Usuário não informado! Erro: {error}'))
            return HttpResponseRedirect(reverse('login'))
        except Exception as error:
            message = _("Opss... Ocorreu um erro inesperado! ") + f"Erro: {error}"
            messages.error(request, message=message)
            return HttpResponseRedirect(reverse("login"))

        try:
            user = User.objects.get(username=username)
            messages.success(request, _("Para continuar o login, informe sua senha"))
            return HttpResponseRedirect(reverse('validate_password', kwargs={'user': encrypt_name(user.username)}))
        except ObjectDoesNotExist as error:
            messages.error(request, _(f'Usuário não encontrado: Erro: {error}'))
        except Exception as error:
            message = _("Opss... Ocorreu um erro inesperado! ") + f"Erro: {error}"
            messages.error(request, message=message)

        return HttpResponseRedirect(reverse("login"))

    messages.error(request, _("Método de requisão não permitido!"))
    return HttpResponseRedirect(reverse('login'))


def validate_password(request, user):
    try:
        user_normal = User.objects.get(username=decrypt_name(user))
    except Exception as error:
        message = _("Opss... Ocorreu um erro ao validar o login, tente novamente!") + f"Erro: {error}"
        messages.error(request, message=message)
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'registration/loginPassword.html', {"user": user})



# verfica a senha e se é compativel com email, se for valido redireciona para escolher a empresa
def login_in_system(request):
    try:
        user = request.POST.get('user')
        p = request.POST.get('password')
    except Exception as error:
        message = _("Opss... Ocorreu um erro ao valida o login, tente novamente!") + f"Erro: {error}"
        messages.error(request, message=message)
        return HttpResponseRedirect(reverse('login'))

    try:
        user = User.objects.get(username=decrypt_name(user))

        if check_password(p, user.password):
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request, _("Senha errada, revise e tente novamente!"))
            return HttpResponseRedirect(reverse("validate_password", kwargs={"user": user}))

    except ObjectDoesNotExist:
        messages.error(request, _(f"Usuário não encontrado, verifique os dados e tente novamente!"))
        return HttpResponseRedirect(reverse("login"))

    except Exception as error:
        message = _("Opss... Ocorreu um erro ao valida o login, tente novamente!") + f"Erro: {error}"
        messages.error(request, message=message)
        return HttpResponseRedirect(reverse('login'))

@login_required()
def register(request):
    if request.method == 'POST':

        if request.user.is_superuser:
            form = RegisterForm(request.POST)
            nameGroups = AuthGroup.objects.all()

        else:
            form = RegisterForm(request.POST)
            nameGroups = AuthGroup.objects.all().exclude(name="Api")

        if form.is_valid():
            form.save()
            # dados do usuario
            user = User.objects.get(username=request.POST['username'])

            logTerms = TableLog(termsOfPrivacy=0, userId=user.id)
            logTerms.save()

            # dados group
            userGroup = AuthGroup.objects.get(name=request.POST['group'])

            if user:
                # control API - USERS
                if userGroup.name == "Api" or userGroup.id == 1:
                    control = ControlApi(user=user, group=userGroup, reg_ativo=1)
                    control.save()
                else:
                    pass

                messages.success(request, _(f'Usuario {user.username} foi adicionado ao grupo de {userGroup.name} !'))
                return redirect('login')

    else:
        if request.user.is_superuser:
            form = RegisterForm(request.POST)
            nameGroups = AuthGroup.objects.all()
        else:
            form = RegisterForm(request.POST)
            nameGroups = AuthGroup.objects.all().exclude(name="Api")

    return render(request, "registration/register.html", {"form": form, 'grupos': nameGroups})


def validate_username(request):
    username = request.GET.get('username', None)

    data = {
        'existe': User.objects.filter(username__iexact=username).exists()
    }

    if data['existe']:
        data['error_message'] = _('Esse usúario já existe')
    return JsonResponse(data)