from django.urls import path
from Producao.views import ProducaoCreate, list_production


urlpatterns = [
    path('<date_min>&<date_max>', list_production, name='list_producao'),
    path('create', ProducaoCreate.as_view(), name='create_producao')

]