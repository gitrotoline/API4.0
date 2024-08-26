from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from API.Permissions_api import ApenasApi
from Receitas.models import DbRecipe, DbRecipe_data
from Receitas.serializer import Recipe_Serializer, Recipe_Data_Serializer


# ------------------------------------ RECEITA -------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_receita(request):
    try:
        queryset = DbRecipe.objects.all()
        serializer = Recipe_Serializer(queryset, many=True)
        print(f"\nDados Retornados das Receitas: {len(queryset)} dados.")
        return Response(serializer.data)
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})


# CREATE RECEITA - MÉTODO POST
class ReceitaCreate(generics.CreateAPIView, LoginRequiredMixin):
    permission_classes = [IsAuthenticated, ApenasApi]
    serializer_class = Recipe_Serializer
    queryset = DbRecipe.objects.all()
    def post(self, request):
        try:
            print(f"\nReceita sendo criada.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])

# ------------------------------------ MÉTODO AUXILIAR UPDATE ----------------------------------------------------------
# UPDATE AND DELETE, code reutilizado
class UpdateAndDelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

# ------------------------------------ FIM DO AUXILIAR MÉTODO UPDATE ---------------------------------------------------

class ReceitaUpdate(UpdateModelMixin, GenericAPIView):
    lookup_field = 'recipeID'
    permission_classes = [IsAuthenticated, ApenasApi]
    serializer_class = Recipe_Serializer
    queryset = DbRecipe.objects.all()

    def put(self, request, recipeID):
        try:
            print(f"\nReceita sendo atualizada.")
            return self.update(request, recipeID)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def recipe_id(request, recipeID):
    try:
        queryset = DbRecipe.objects.filter(recipeID=recipeID)
        serializer = Recipe_Serializer(queryset, many=True)
        print(f"Pesquisa pela recipe: id da receita => {recipeID}")
        return Response(serializer.data)
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})

# ------------------------------------- FIM DA RECEITA -----------------------------------------------------------------


# ----------------------------------- ENDPOINT RECIPE DATA ------------------------------------------------------------
# LISTA RECEITA DATA POR ID- MÉTODO GET
@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def list_dbrecipe_data_por_id(request, recipeID):
    try:
         queryset = DbRecipe_data.objects.filter(recipeID_id=recipeID)
         print(f"\nDados Retornados de Dados da Receita: id:{recipeID}, {len(queryset)} dados.")
         serializer = Recipe_Data_Serializer(queryset, many=True)
         if len(serializer.data) > 0:
             return Response(serializer.data)
         else:
             return Response({"NOT DATA": _("Not data was found with this parameter!")})
    except Exception as error:
         return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})

@api_view(['GET'])
@permission_classes([IsAuthenticated, ApenasApi])
def recipe_dados_por_evento(request, recipeID, event):
    try:
        queryset = DbRecipe_data.objects.filter(recipeID_id=recipeID, evento=event)
        print(f"\nDados Retornados de Dados da Receita por id e evento: id:{recipeID}, {len(queryset)} dados.")
        serializer = Recipe_Data_Serializer(queryset, many=True)
        if len(serializer.data) > 0:
            return Response(serializer.data)
        else:
            return Response({"NOT DATA": _("Not data was found with this parameter!")})
    except Exception as error:
        return Response({"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")})



@api_view(['PUT'])
@permission_classes([ApenasApi])
def update_recipe_data(request, recipeID, event):
    try:
        recipeData = get_object_or_404(DbRecipe_data, evento=event, recipeID=recipeID)
        serializer = DbRecipe_data(recipeData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Dados Ataualizados")
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])


# RECEITA DATA CREATE - MÉTODO PUT
class Recipe_dataCreate(generics.CreateAPIView, LoginRequiredMixin):
    lookup_field = 'recipeID_id'
    permission_classes = [IsAuthenticated, ApenasApi]
    serializer_class = DbRecipe_data
    queryset = DbRecipe_data.objects.all()

    def post(self, request):
        try:
            print(f"\nDados da Receita sendo criada.")
            return self.create(request)
        except Exception as error:
            return Response([{"ERROR": _(f"An unexpected error has occurred. Error => {str(error)}")}])

# -------------------------------------- FIM RECEITA DATA --------------------------------------------------------------