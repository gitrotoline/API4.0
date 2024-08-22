from django.urls import path
from Receitas.views import recipe_dados_por_evento, Recipe_dataCreate, list_dbrecipe_data_por_id, update_recipe_data

urlpatterns = [

    path('<int:recipeID>', list_dbrecipe_data_por_id, name='dados_receita_por_id'),
    path('event/<int:recipeID>&<str:event>', recipe_dados_por_evento, name="dados_receita_eventos"),
    path('update/<int:recipeID>&<str:event>', update_recipe_data, name='dados_recipe_update'),
    path('create', Recipe_dataCreate.as_view(), name='dados_recipe_create')

]
