# --------------------------------- ENDPOINT RWTC ----------------------------------------------------------------------
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from API.Permissions_api import Admin
from Rwtc.models import RWTC
from Rwtc.serializer import RWTC_serializer


@api_view(['GET'])
def list_rwtc(request, date_min, date_max):
    try:
        queryset = RWTC.objects.filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados do RWTC ---- {len(queryset)} dados")
        serializer = RWTC_serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


class Rwtc_create(generics.CreateAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = RWTC_serializer
    queryset = RWTC.objects.all()

    def post(self, request):
        try:
            print(f"\nDados de sensor do RWTC sendo gravado.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_rwtc_cart(request, number_cart, date_min, date_max):
    try:
        queryset = RWTC.objects.filter(cart=f"C{number_cart}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados do RWTC do CARRO {number_cart} --> {len(queryset)}")
        serializer = RWTC_serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])

@api_view(['GET'])
def list_rwtc_station_oven(request, number_cart, date_min, date_max):
    try:
        queryset = RWTC.objects.filter(cart=f"C{number_cart}", station="OVEN", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados do RWTC na estação do FORNO do CARRO {number_cart} ---- {len(queryset)} dados")
        serializer = RWTC_serializer(queryset, many=True)
        return Response(serializer.data)

    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_rwtc_station_precooling(request, number_cart, date_min, date_max):
    try:
        queryset = RWTC.objects.filter(cart=f"C{number_cart}", station="PRE_COOLING", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados do RWTC na estação do PRE - RESFRIAMENTO do CARRO {number_cart} ---- {len(queryset)} dados")
        serializer = RWTC_serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
def list_rwtc_station_cooling(request, number_cart, date_min, date_max):
    try:
        queryset = RWTC.objects.filter(cart=f"C{number_cart}", station="COOLING", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados do RWTC na estação do RESFRIAMENTO do CARRO {number_cart} ---- {len(queryset)} dados")
        serializer = RWTC_serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])

# ----------------------------- ENDPOINT RWTC -------------------------------------------------------------------