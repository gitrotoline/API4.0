import re
import jwt
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.exceptions import ValidationError
from API import settings
from Alarmes.models import Allevent
from Alarmes.serializer import Alarme_serializer, Alarmes_Create_Serializer
from API.Permissions_api import ApenasApi, Admin, retorna_user_api
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Usuario.models import Machines_API, User_Acess_Machines


@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_alarmes(request, machine, date_min, date_max):
    try:
        user_access = retorna_user_api(request)

        if "Error" in user_access:
            return Response({"Error": user_access["Error"]})

        user = user_access["User"]

        # Lista de máquinas válidas
        machines = Machines_API.objects.filter(status=1).values_list('n_serie', flat=True)

        # Validar o formato da máquina
        if not re.match(r'^M\d{1,3}$', machine):
            if machine == "TESTE":
                pass
            else:
                error_message = (
                    'Invalid machine format. The correct format is "www.rotoapi.com/{your machine serial number}", '
                    'the nomenclature of your machine serial number is "M" + "serial number" = (M0, M1, M300, M500 ...). '
                    'Example: www.rotoapi.com/M500'
                )
                return Response({'InvalidMachine': _(error_message)})

        # Verificar se a máquina está na lista de máquinas válidas
        if machine not in machines:
            return Response({'MachineNotFound': _("Your machine is not found!")})

        # Verificar se o usuário tem acesso à máquina
        machine_db = Machines_API.objects.get(n_serie=machine)
        try:
            access_liberado = User_Acess_Machines.objects.get(user=user, machine=machine_db)
        except ObjectDoesNotExist:
            if not user.is_superuser:
                return Response({'AccessNotFound': _("Access for your user is not found! Informe os administradores!")})

        # Consultar o banco de dados correto usando o alias
        db_alias = machine
        queryset = Allevent.objects.using(db_alias).filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados de Alarmes: {len(queryset)} dados.")

        # Serializar os dados
        serializer = Alarme_serializer(queryset, many=True)
        return Response(serializer.data)

    except ValidationError as validate:
        return Response({'ValidationError': str(validate)}, status=400)
    except Exception as error:
        print(f"An unexpected error has occurred: {str(error)}")
        return Response({"Error": _(f"An unexpected error has occurred. Error => {str(error)}")}, status=500)



@api_view(['POST'])
@permission_classes([IsAuthenticated, Admin])  # Adjust Admin as needed
def alarmes_create(request):
    if request.method == 'POST':
        try:

            print("\nDados de Alarme sendo gravado.")
            print(settings.TIME_ZONE)
            print(settings.USE_TZ)

            serializer = Alarmes_Create_Serializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            print(error)
            return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
