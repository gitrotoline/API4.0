from django.urls import path
from Rwtc.views import (list_rwtc, Rwtc_create, list_rwtc_cart, list_rwtc_station_oven, list_rwtc_station_precooling,
                        list_rwtc_station_cooling)

urlpatterns = [
    path('<date_min>&<date_max>', list_rwtc, name='list_rwtc'),
    path('create', Rwtc_create.as_view(), name='rtwc_create'),

    path("CART<int:number_cart>/<date_min>&<date_max>", list_rwtc_cart, name="list_rtwc_car"),
    path("STATION_OVEN/CART<int:number_cart>/<date_min>&<date_max>", list_rwtc_station_oven, name="list_rtwc_station_oven"),
    path("STATION_PRE_COOLING/CART<int:number_cart>/<date_min>&<date_max>", list_rwtc_station_precooling, name="list_rtwc_station_precooling"),
    path("STATION_COOLING/CART<int:number_cart>/<date_min>&<date_max>", list_rwtc_station_cooling, name="list_rtwc_station_cooling")
]