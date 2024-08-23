import re

import jwt
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Permission, Group
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response
from API import settings
from Usuario.models import AuthGroup, ControlApi, Machines_API, User_Acess_Machines, Token_user


def retorna_user_api(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token.get('user_id')
        user = User.objects.get(id=user_id)
        return {"User": user}
    except jwt.ExpiredSignatureError:
        return {"Error": "Your token expired"}
    except jwt.DecodeError:
        return {"Error": "Erro ao decodificar o token"}
    except User.DoesNotExist:
        return {"Error": "User not found!"}
    except Exception as e:
        return {"Error": str(e)}


def validate_machine_format(machine):
    if not re.match(r'^M\d{1,3}$', machine):
        return False, _(
            'Invalid machine format. The correct format is "M" + "serial number" = (M0, M1, M300, M500 ...).')
    return True, None


def get_valid_machines():
    return Machines_API.objects.filter(status=1).values_list('n_serie', flat=True)


def check_user_access(user, machine):
    try:
        machine_db = Machines_API.objects.get(n_serie=machine)
        User_Acess_Machines.objects.get(user=user, machine=machine_db)
        return True
    except ObjectDoesNotExist:
        return False


def get_machine_db_alias(machine):
    # Assuming `machine` directly maps to the database alias
    return machine


class Admin(BasePermission):
    def has_permission(self, request, view):

        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header:
            try:
                token = auth_header.split(' ')[1]
                # indentifica se o token foi gerado pela aplicacao que está sendo consultada
                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                # get user id in json token
                user_id = decoded_token.get('user_id')
                # query in USER
                user = User.objects.get(id=user_id)
                # get credentials no controle da API
                if user.is_superuser == 1: return True
                else: return False
            except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidTokenError) as error:
                raise AuthenticationFailed(_('Token de autenticação inválido.', error))
        else:
            return Response([{"Error": "Try again request"}])


# its my obra prima

class ApenasApi(BasePermission):
    def has_permission(self, request, view):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header:
            token = self.get_token_from_header(auth_header)
            try:
                user = self.get_user_from_token(token)
                if user.is_superuser or self.is_user_in_api_group(user):
                    return True

            except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidTokenError) as error:
                print("Invalid token:", error)
                raise AuthenticationFailed(_('Invalid authentication token.'))
            except ObjectDoesNotExist as error:
                print("Object not found:", error)
                raise AuthenticationFailed(_('User or group not found.'))
        else:
            if request.user.is_authenticated and request.user.is_superuser:
                return True
            if self.is_user_in_api_group(request.user):
                return True

        return Response([{"Not Access": "Your user has restricted access, please report to the administrator for more ""information"}])

    def get_token_from_header(self, auth_header):
        return auth_header.split(' ')[1]

    def get_user_from_token(self, token):
        # Verifica se o token existe no banco
        try:
            token_record = Token_user.objects.get(token=token)
        except Token_user.DoesNotExist:
            print("aquii")
            raise AuthenticationFailed(_('Token inválido. Gere o token e adicione no cabeçalhos das requisições. Para gerar o token use o endpoint /api_token que ira retorna o token de acesso.'))

        # Decodifica o token para obter o usuário
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token.get('user_id')
        return User.objects.get(id=user_id)

    def is_user_in_api_group(self, user):
        api_group = Group.objects.get(name='Api')
        control_api = ControlApi.objects.get(user=user, group=api_group)
        return control_api.reg_ativo



schema_view = get_schema_view(
    openapi.Info(
        title="Rotoline API",
        default_version='4.0.0',
        description=_('<h2>API that provides data from your <b>ROTOLINE MACHINE</b><h2>'

                      '<div>'
                      '<h6>With the ***API you can obtain data from your Machine***, such as ***Cycles, Alarms, Production Data***, among others. '
                      'This data is returned in **JSON format (a universal data format - {key: value})**, which can be processed and used according to your needs. Some examples include dashboards, production monitoring, '
                      'system development, or generating metrics for your system.'
                      '</h6>'
                      '</div>'

                      '<div><h6>The API is divided into **ENDPOINTS** - **(Alarms, Hourmeters, Weighing, '
                      'Production, Recipes, Sensor, Timeline, and Token)**</h6></div>'

                      '<div></h4>- <b>**ENDPOINTS** that retrieve data directly from the Machine database:</b></h4></div><br>'
                      '<div>'
                      '<ul>'
                      '<li> <b>***ALARMS***: <i>Returns the alarms from the machine.</i></b></li>'
                      '<li> <b>***RECIPES***: Returns the recipes.</b></li>'
                      '<li> <b>***HOURMETERS***: <i>Returns the hourmeter data from the machine.</i></b></li>'
                      '<li> <b>***WEIGHING***: <i>If the machine has a weighing system, returns the weighing data from the machine.</i></b></li>'
                      '<li> <b>***PRODUCTION***: <i>Returns the cycle data report from the machine, such as (Cycle Duration, Oven Duration, etc.).</i></b></li>'
                      '<li> <b>***SENSOR***: <i>Returns the sensors that occur in the machine</i></b></li>'
                      '<li> <b>***TIMELINE***: <i>Returns each stage of the cycle - (LOADING, OVEN, COOLING, PRE-COOLING, and UNLOADING)., '
                      'which car is in the stage, and the start time of the stage, in a timeline format as the stages occur.</i></b></li><br>'


                      '</ul>'
                      '</div>'

                      '<div><h4>- The **ENDPOINTS** for using the **API** through other services:</h4></div>'
                      '<div><i><b>Access is granted by logging into the application with the following credentials (USERNAME and PASSWORD).</b></i></div><br>'

                      '<div><ul><li><b>After logging into the application, at the url path - example: "m000-app.rotoline.com/api_token", two tokens are generated:<b></li></ul></div>'

                      '<ul>'
                      '<li>**ACCESS TOKEN**: <i>Access token for API queries through services that perform this operation or through a script developed to query this endpoint.'
                      '<ul><li> This token has a duration of 4 hours</li></ul>'
                      '</li>'
                      '</ul>'


                      '<ul>'
                      '<li>**REFRESH TOKEN**: <i>If the token needs to be refreshed, it is done using the refresh token.'
                      '<ul><li> The refresh token is valid for 1 day</li></ul>'
                      '</li>'
                      '</ul>'),

        terms_of_service="https://rotoline.com",
        contact=openapi.Contact(
            name='Suporte a Desenvolvedores',
            email="support@rotoline.com",
            url="https://www.rotoline.com/br/suporte-tecnico/", ),

        license=openapi.License(
            name="Licença GPLv3",
            url="https://www.gnu.org/licenses/gpl-3.0.html", ),
    ),

    public=True,  # se False, inclui apenas endpoints aos quais o usuário atual tem acesso
    permission_classes=(ApenasApi, IsAuthenticated),  # somente usuario autenticado pode visualizar
    authentication_classes=(BasicAuthentication, SessionAuthentication),
)

