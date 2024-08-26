# --------------------------------- ENDPOINT AMPS ---------------------------------------------------------------------
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from API.Permissions_api import Admin
from Corrente.models import Corrente_Eletrica
from Corrente.serializer import Corrente_Eletrica_serializer


@api_view(['GET'])
def list_amps(request, date_min, date_max):
    try:
        queryset = Corrente_Eletrica.objects.filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de Corrente ---- {len(queryset)} dados")
        serializer = Corrente_Eletrica_serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


class Amps_create(generics.CreateAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = Corrente_Eletrica_serializer
    queryset = Corrente_Eletrica.objects.all()

    def post(self, request):
        try:
            print(f"\nDados de sensor de corrente sendo gravado.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_amps_all_cart(request, number_cart, date_min, date_max):
    try:
        queryset = Corrente_Eletrica.objects.filter(cart=f"C{number_cart}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de Corrente do CARRO {number_cart} ---- {len(queryset)} dados")
        serializer = Corrente_Eletrica_serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_amps_arm(request, number_arm, date_min, date_max):
    try:
        queryset = Corrente_Eletrica.objects.filter(sensor=f"ARM{number_arm}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de Corrente do BRAÇO {number_arm} ---- {len(queryset)} dados")
        serializer = Corrente_Eletrica_serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_amps_plate(request, number_plate, date_min, date_max):
    try:
        queryset = Corrente_Eletrica.objects.filter(sensor=f"PLATE{number_plate}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de Corrente do PRATO {number_plate} -> {len(queryset)} dados")
        serializer = Corrente_Eletrica_serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_amps_cart(request, number_cart, date_min, date_max):
    try:
        queryset = Corrente_Eletrica.objects.filter(sensor=f"CART{number_cart}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de Corrente(Sensor) do CARRO {number_cart} ---- {len(queryset)} dados")
        serializer = Corrente_Eletrica_serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])
# ----------------------------- ENDPOINT AMPS -------------------------------------------------------------------------