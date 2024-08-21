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


@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_alarmes(request, date_min, date_max):
    try:

        queryset = Allevent.objects.filter(datetime__range=(date_min, date_max)).order_by('datetime')
        print(f"\nDados Retornados de Alarmes:  {len(queryset)} dados.")
        serializer = Alarme_serializer(queryset, many=True)
        return Response(serializer.data)

    except ValidationError:
        return Response({'ValidationError': _("The date format entered is incorrect, Please try: the format YYYY-MM-DD hh:mm - (year-month-day hours:minutes)")})
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
