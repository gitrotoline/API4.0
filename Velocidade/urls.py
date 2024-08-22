from django.urls import path
from Velocidade.views import list_speed, Speed_create, list_speed_cart, list_speed_arm, \
    list_speed_plate, list_speed_all_cart

urlpatterns = [
    path('<date_min>&<date_max>', list_speed, name='list_sensor_speed'),
    path('create', Speed_create.as_view(), name='speed_create'),

    path("CART<int:number_cart>/<date_min>&<date_max>", list_speed_cart, name="list_speed_cart"),
    path("ARM<int:number_arm>/<date_min>&<date_max>", list_speed_arm, name="list_speed_arm"),
    path("PLATE<int:number_plate>/<date_min>&<date_max>", list_speed_plate, name="list_speed_plate"),
    path("ALL_CART<int:number_cart>/<date_min>&<date_max>", list_speed_all_cart, name="list_speed_all_cart")

]