from django.urls import path
from Temperatura.views import list_temperature, Temperature_create, list_temperature_cart

urlpatterns = [
    path('<date_min>&<date_max>', list_temperature, name='list_temperature'),
    path('create', Temperature_create.as_view(), name='temperature_create'),
    path("CART<int:number_cart>/<date_min>&<date_max>", list_temperature_cart, name="list_temperature_cart")
]