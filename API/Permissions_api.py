import jwt
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Permission
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from API import settings
from Usuario.models import AuthGroup, AuthUserGroups, ControlApi



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
                if user.is_superuser == 1:
                    return True
                else:
                    return False
            except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidTokenError) as error:
                raise AuthenticationFailed(_('Token de autenticação inválido.', error))
        else:
            print('aqui')


# class de permissão ao acesso a API
class ApenasApi(BasePermission):
    def has_permission(self, request, view):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header:
            try:
                token = auth_header.split(' ')[1]

                # indentifica se o token foi gerado pela aplicacao que está sendo consultada
                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

                # get user id in json token
                user_id = decoded_token.get('user_id')

                # query get id group
                group_id = AuthGroup.objects.get(name='Api')

                # query in USER
                user = User.objects.get(id=user_id)

                # get credentials no controle da API
                if user.is_superuser == 1:
                    return True

                else:
                    # query in GROUP
                    group = AuthGroup.objects.get(id=group_id.id)

                    # User e Group
                    user_and_group = AuthUserGroups.objects.get(user_id=user.id)

                    control_api = ControlApi.objects.get(user_id_id=user.id, group_user_id_id=group.id)

                    if user_and_group.group_id == group.id and control_api.reg_ativo == 1:
                        return True

                    else:
                        return False

            except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidTokenError) as error:
                raise AuthenticationFailed(_('Token de autenticação inválido.'))
            except ObjectDoesNotExist as error:
                raise AuthenticationFailed(_('Usuário ou grupo não encontrado.'))
        else:
            if request.user.is_superuser == 1 or request.user.is_superuser == True:
                return True
            else:
                # query get id group
                group_id = AuthGroup.objects.get(name='Api')

                # query in USER
                user = User.objects.get(id=request.user.id)

                # query in GROUP
                group = AuthGroup.objects.get(id=group_id.id)

                # User e Group
                user_and_group = AuthUserGroups.objects.get(user_id=user.id)

                # get credentials no controle da API
                control_api = ControlApi.objects.get(user_id_id=user.id, group_user_id_id=group.id)

                if user_and_group.group_id == group.id and control_api.reg_ativo == 1:
                    return True
                else:
                    return False


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

