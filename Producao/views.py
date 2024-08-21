from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from API.Permissions_api import ApenasApi, Admin
from Producao.models import Relatorioresumido
from Producao.serializer import Producao_Serializer_GET, Producao_Serializer
from django.utils.translation import gettext_lazy as _


# LISTA PRODUÇÃO / MÉTODO GET
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_production(request, date_min, date_max):
    try:
        queryset = Relatorioresumido.objects.filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados de Produção:  {len(queryset)} dados.")
        serializer = Producao_Serializer_GET(queryset, many=True)

        return Response(serializer.data)
    except ValidationError:
        return Response({'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")})
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {error}")})


class ProducaoCreate(generics.CreateAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = Producao_Serializer
    queryset = Relatorioresumido.objects.all()

    def post(self, request):
        print(f"\nDados da Producao sendo gravado.")
        return self.create(request)
