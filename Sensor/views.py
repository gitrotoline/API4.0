# LIST DE TODOS OS SENSORES / API
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from API.Permissions_api import ApenasApi, Admin
from Sensor.models import Sensor
from Sensor.serializer import Sensor_Serializer_GET, Sensor_Serializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_sensor(request, date_min, date_max):
    try:
        queryset = Sensor.objects.filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados do Sensor - GERAL: {len(queryset)} dados.")
        serializer = Sensor_Serializer_GET(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


#  SENSOR - MÉTODO POST
class SensorCreate(generics.CreateAPIView, LoginRequiredMixin):
    """This endpoint is for internal API control use only, the client is not allowed to use this endpoint"""
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = Sensor_Serializer
    queryset = Sensor.objects.all()

    def post(self, request):
        try:
            print(f"\nDados de Sensor sendo gravado.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


# SENSOR PORTA 01 ABERTA - METODO GET POR DATETIME
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_sensor_porta01_aberta(request, date_min, date_max):
    try:
        queryset = Sensor.objects.filter(sensor='FC1').filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados do Sensor da Porta 01 - Aberta FC1: {len(queryset)} dados.")
        serializer = Sensor_Serializer_GET(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


# SENSOR PORTA 01 FECHADA - METODO GET POR DATETIME
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_sensor_porta01_fechada(request, date_min, date_max):
    try:
        queryset = Sensor.objects.filter(sensor='FC2').filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados do Sensor da Porta 01 - Fechada FC2: {len(queryset)} dados.")
        serializer = Sensor_Serializer_GET(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


# SENSOR PORTA 02 ABERTA - METODO GET POR DATETIME
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_sensor_porta02_aberta(request, date_min, date_max):
    try:
        queryset = Sensor.objects.filter(sensor='FC3').filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados do Sensor da Porta 02 - Aberta FC3: {len(queryset)} dados.")
        serializer = Sensor_Serializer_GET(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


# SENSOR PORTA 02 FECHADA - METODO GET POR DATETIME
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_sensor_porta02_fechada(request, date_min, date_max):
    try:
        queryset = Sensor.objects.filter(sensor='FC4').filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados do Sensor da Porta 02 - Fechada FC4: {len(queryset)} dados.")
        serializer = Sensor_Serializer_GET(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})



# SENSOR ESCOTILHA 01 ABERTA - METODO GET POR DATETIME
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_sensor_escotilha01_aberta(request, date_min, date_max):
    try:
        queryset = Sensor.objects.filter(sensor='S45').filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados do Sensor da Escotilha 01 - Aberta S44: {len(queryset)} dados.")
        serializer = Sensor_Serializer_GET(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


# SENSOR ESCOTILHA 01 FECHADA - METODO GET POR DATETIME
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_sensor_escotilha01_fechada(request, date_min, date_max):
    try:
        queryset = Sensor.objects.filter(sensor='S43').filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados do Sensor da Escotilha 01 - Fechada S43: {len(queryset)} dados.")
        serializer = Sensor_Serializer_GET(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})



@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_sensor_escotilha02_aberta(request, date_min, date_max):
    try:
        queryset = Sensor.objects.filter(sensor='S46').filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados do Sensor da Escotilha 02 - Aberta S46: {len(queryset)} dados.")
        serializer = Sensor_Serializer_GET(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


# SENSOR ESCOTILHA 02 FECHADA - METODO GET POR DATETIME
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_sensor_escotilha02_fechada(request, date_min, date_max):
    try:
        queryset = Sensor.objects.filter(sensor='S44', datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados do Sensor da Escotilha 02 - Fechada S44: {len(queryset)} dados.")
        serializer = Sensor_Serializer_GET(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})
# ---------------------------------- FIM DO SENSOR ---------------------------------------------------------------------
