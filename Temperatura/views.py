from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from API.Permissions_api import Admin
from Temperatura.models import DbTemperature
from Temperatura.serializer import Temperature_Serializer


@api_view(['GET'])
def list_temperature(request, date_min, date_max):
    try:
        queryset = DbTemperature.objects.filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de Temperatura ---- {len(queryset)} dados")
        serializer = Temperature_Serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


class Temperature_create(generics.CreateAPIView, LoginRequiredMixin):

    permission_classes = [IsAuthenticated, Admin]
    serializer_class = Temperature_Serializer
    queryset = DbTemperature.objects.all()

    def post(self, request):
        try:
            print(f"\nDados de sensor de temperature sendo gravado.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])

@api_view(['GET'])
def list_temperature_cart(request, number_cart, date_min, date_max):
    try:
        queryset = DbTemperature.objects.filter(cart=f"C{number_cart}", datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"Retornando dados de Temperatura do CARRO {number_cart} ---- {len(queryset)} dados")
        serializer = Temperature_Serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _(
            "The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])

# ----------------------------- ENDPOINT TEMPERATURE -------------------------------------------------------------------