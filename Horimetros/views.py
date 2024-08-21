from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from API.Permissions_api import ApenasApi, Admin
from Horimetros.models import DbHorimeter
from Horimetros.serializer import Horimeter_Serializer
from django.utils.translation import gettext_lazy as _


@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_horimeter(request):
    try:
        queryset = DbHorimeter.objects.all()
        serializer = Horimeter_Serializer(queryset, many=True)
        print(f"\nDados Retornados dos Horimetros: {len(queryset)} dados.")
        return Response(serializer.data)
    except Exception as error:
        print(error)
        return Response({"ERROR": f"An unexpected error has occurred. Error => {error}"}, status=500)



@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_horimeter_per_machine_and_name(request, machine, name):
        try:
            queryset = DbHorimeter.objects.filter(machineID=machine, nome=name)
            serializer = Horimeter_Serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response({"ERROR": _(f"An unexpected error has occurred. Error => {error}")})


# HORIMETROS - MÉTODO POST
class HorimeterCreate(generics.CreateAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated, Admin]
    serializer_class = Horimeter_Serializer
    queryset = DbHorimeter.objects.all()

    def post(self, request):
        try:
            print(f"\nDados de Horimetro sendo gravado.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error: {error}")}])


@api_view(['PUT'])
@permission_classes([Admin])
def update_horimeter_per_machine_and_name(request, machine, name):
    try:
        horimeter = get_object_or_404(DbHorimeter, nome=name, machineID=machine)
        serializer = Horimeter_Serializer(horimeter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Dados Ataualizados")
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error: {error}")}])

# ------------------------------------ FIM HORIMETROS -----------------------------------------------------------------