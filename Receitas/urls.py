from django.urls import path
from Receitas.views import ReceitaUpdate, ReceitaCreate, list_receita, recipe_id


urlpatterns = [
    path('', list_receita, name='list_receitas'),
    path('create', ReceitaCreate.as_view(), name='create_receita'),
    path('update/<int:recipeID>', ReceitaUpdate.as_view(), name='update_receita'),
    path('<int:recipeID>', recipe_id, name='search_recipeID'),
]



