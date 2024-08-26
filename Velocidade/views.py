# --------------------------------- ENDPOINT SPEED ---------------------------------------------------------------------
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from API.Permissions_api import Admin
from Velocidade.models import Speed
from Velocidade.serializer import Speed_Serializer
from django.utils.translation import gettext_lazy as _


@api_view(['GET'])
def list_speed(request, date_min, date_max):
    try:
        queryset = Speed.objects.filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de velocidade ---- {len(queryset)} dados")
        serializer = Speed_Serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("O Formato da data informada está incorreta, Por Favor, tente: o formato YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERRO": _(f"Ocorreu um erro inesperado. Erro => {str(error)}")}])


class Speed_create(generics.CreateAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = Speed_Serializer
    queryset = Speed.objects.all()

    def post(self, request):
        try:
            print(f"\nDados de sensor de velocidade sendo gravado.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_speed_cart(request, number_cart, date_min, date_max):
    try:
        queryset = Speed.objects.filter(sensor=f"C{number_cart}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de velocidade do CARRO {number_cart} --> {len(queryset)} dados")
        serializer = Speed_Serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_speed_arm(request, number_arm, date_min, date_max):
    try:
        queryset = Speed.objects.filter(sensor=f"ARM{number_arm}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de velocidade do BRAÇO {number_arm} ---- {len(queryset)} dados")
        serializer = Speed_Serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])

@api_view(['GET'])
def list_speed_plate(request, number_plate, date_min, date_max):
    try:
        queryset = Speed.objects.filter(sensor=f"PLATE{number_plate}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de velocidade do PRATO  {number_plate} ) ---- {len(queryset)} dados")
        serializer = Speed_Serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_speed_all_cart(request, number_cart, date_min, date_max):
    try:
        queryset = Speed.objects.filter(cart=f"C{number_cart}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de velocidade do CARRO {number_cart} (all_sensores) ---- {len(queryset)} dados")
        serializer = Speed_Serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])

# ----------------------------- ENDPOINT SPEED -------------------------------------------------------------------------
