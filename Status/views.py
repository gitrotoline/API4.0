from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from API.Permissions_api import ApenasApi, Admin
from Status.models import Status_Machine
from Status.serializer import Status_Serializer


@api_view(['GET'])
@permission_classes([ApenasApi])
def status_machine_view(request):
    try:
        queryset = Status_Machine.objects.get(id=1)
        date = queryset.date
        return Response(
            [{"id": 1, "date": date}]
        )
    except Status_Machine.DoesNotExist:
        return Response([
            {"ERROR": "No status machine found."}
        ])


# UPDTADE RECEITAS - MÉTODO PUT


class Status_update(UpdateModelMixin, GenericAPIView):
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = Status_Serializer
    queryset = Status_Machine.objects.all()

    def put(self, request, pk):
        try:
            queryset = Status_Machine.objects.get(id=pk)
            queryset.date = request.data['date']
            queryset.save()
            print("Atualizando: ", request.data)
            return Response([{"id": queryset.id, "date": queryset.date}])
        except Exception as error:
            print("Erro ao atualizar status: ", str(error))
            return Response([{'ERROR': str(error)}])