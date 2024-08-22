from django.urls import path
from Sensor.views import list_sensor, list_sensor_porta01_aberta, list_sensor_porta01_fechada, list_sensor_porta02_aberta, \
    list_sensor_porta02_fechada, list_sensor_escotilha01_fechada, list_sensor_escotilha01_aberta, list_sensor_escotilha02_fechada, \
    list_sensor_escotilha02_aberta, SensorCreate

urlpatterns = [
    path('<date_min>&<date_max>', list_sensor, name='list_sensor'),
    path('create', SensorCreate.as_view(), name='sensor_create'),

    # SENSOR DAS PORTAS(1 e 2) ABERTAS/FECHADAS
    path('door01_open/<date_min>&<date_max>', list_sensor_porta01_aberta, name='sensor_porta_aberta01'),
    path('door01_closed/<date_min>&<date_max>', list_sensor_porta01_fechada, name='sensor_porta_fechada01'),
    path('door02_open/<date_min>&<date_max>', list_sensor_porta02_aberta, name='sensor_porta_aberta02'),
    path('door02_closed/<date_min>&<date_max>', list_sensor_porta02_fechada, name='sensor_porta_fechada02'),

    # SENSOR ESCOTILHAS (1 e 2) ABERTAS/FECHADAS
    path('hatch01_open/<date_min>&<date_max>', list_sensor_escotilha01_fechada, name='sensor_escoltilha_aberta01'),
    path('hatch01_closed/<date_min>&<date_max>', list_sensor_escotilha01_aberta, name='sensor_escotilha_fechada01'),
    path('hatch02_open/<date_min>&<date_max>', list_sensor_escotilha02_fechada, name='sensor_escotilha_aberta02'),
    path('hatch02_closed/<date_min>&<date_max>', list_sensor_escotilha02_aberta, name='sensor_escotilha_fechada02'),
]