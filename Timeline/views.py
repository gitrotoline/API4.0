from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from API.Permissions_api import ApenasApi, Admin
from Timeline.models import DbTimeline_sensores, DbTimeline, DbTimelineDados
from Timeline.serializer import TimeLine_Serializer, TimeLine_Dados_Serializer, TimeLine_CLP_Serializer


@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_timeline(request, date_min, date_max):
    try:
        queryset = DbTimeline.objects.filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados da Timeline: {len(queryset)} dados.")
        serializer = TimeLine_Serializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})



class TimelineCreate(generics.CreateAPIView, LoginRequiredMixin):
    """This endpoint is for internal API control use only, the client is not allowed to use this endpoint"""
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = TimeLine_Serializer
    queryset = DbTimeline.objects.all()

    def post(self, request):
        try:
            print(f"\nDados da Timeline sendo gravado.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])

# --------------------------------------- FIM DA TIMELINE   ------------------------------------------------------------


# ---------------------------------------TIMELINE DADOS  ---------------------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_timeline_dados(request, id_ciclo):
    try:
        queryset = DbTimelineDados.objects.filter(ciclo=id_ciclo)
        print(f"\nDados da Timeline retornados: {len(queryset)} dados.")
        serializer = TimeLine_Dados_Serializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


#  TIMELINE DADOS - MÉTODO POST
class TimelineDadosCreate(generics.CreateAPIView, LoginRequiredMixin):
    """This endpoint is for internal API control use only, the client is not allowed to use this endpoint"""
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = TimeLine_Dados_Serializer
    queryset = DbTimelineDados.objects.all()

    def post(self, request):
        try:
            print(f"\nDados da Timeline Dados sendo gravado.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


# --------------------------------------- FIM DA TIMELINE DADOS  -------------------------------------------------------


# -------------------------------------- TIMELINE DADOS SENSORES -------------------------------------------------------
# LIST TIMELINE / API
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_timeline_sensores(request, date_min, date_max):
    try:
        queryset = DbTimeline_sensores.objects.filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados da Timeline_sensores: {len(queryset)} dados.")
        serializer = TimeLine_CLP_Serializer(queryset, many=True)
        return Response(serializer.data)
    except ValidationError:
        return Response([{'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")}])
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


#  TIMELINE DADOS - MÉTODO POST
class TimelineDados_sensoresCreate(generics.CreateAPIView, LoginRequiredMixin):
    """This endpoint is for internal API control use only, the client is not allowed to use this endpoint"""
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = TimeLine_CLP_Serializer
    queryset = DbTimeline_sensores.objects.all()

    def post(self, request):
        try:
            print(f"\nDados da Timeline => sensores sendo gravado.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])
# --------------------------------------- FIM DA TIMELINE DADOS DE SENSORES --------------------------------------------
