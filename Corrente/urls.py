from django.urls import path
from Corrente.views import list_amps, Amps_create, list_amps_all_cart, list_amps_arm, list_amps_plate, list_amps_cart


urlpatterns = [
    path('<date_min>&<date_max>', list_amps, name='list_sensor_amps'),
    path('create', Amps_create.as_view(), name='amps_create'),
    path('ARM<int:number_arm>/<date_min>&<date_max>', list_amps_arm, name="list_sensor_amps_arm"),
    path('PLATE<int:number_plate>/<date_min>&<date_max>', list_amps_plate, name="list_sensor_amps_plate"),
    path('CART<int:number_cart>/<date_min>&<date_max>', list_amps_cart, name="list_sensor_amps_cart"),
    path('ALL_CART<int:number_cart>/<date_min>&<date_max>', list_amps_all_cart, name="list_sensor_amps_all_cart")
]