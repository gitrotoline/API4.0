from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from API import settings
from Alarmes.models import Allevent
from Alarmes.serializer import Alarme_serializer, Alarmes_Create_Serializer
from API.Permissions_api import ApenasApi, Admin
from django.utils.translation import gettext_lazy as _
from django.db import connections
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import re


@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_alarmes(request, machine, date_min, date_max):
    # Lista de máquinas válidas
    machines = ["M442", "M365", "M453", "M407", "M508", "M537", "M567"]

    # Validar o formato da máquina
    if not re.match(r'^M\d{1,3}$', machine):
        return Response({'error': _("Invalid machine format.")}, status=404)

    # Verificar se a máquina está na lista de máquinas válidas
    if machine not in machines:
        return Response({'error': _("Machine not found.")}, status=404)

    try:
        # Definir o banco de dados correto com base na máquina
        db_alias = machine

        # Consultar o banco de dados correto usando o alias
        queryset = Allevent.objects.using(db_alias).filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados de Alarmes: {len(queryset)} dados.")

        # Serializar os dados
        serializer = Alarme_serializer(queryset, many=True)

        # Retornar a resposta com os dados serializados
        return Response(serializer.data)
    except ValidationError as validate:
        return Response({'ValidationError': str(validate)})
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


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
