from django.urls import path
from .views import list_horimeter, HorimeterCreate, list_horimeter_per_machine_and_name, update_horimeter_per_machine_and_name

urlpatterns = [
    path('', list_horimeter, name='list_horimeter'),
    path('<str:machine>&<str:name>', list_horimeter_per_machine_and_name, name='horimeter_per_machine_and_name'),
    path('create', HorimeterCreate.as_view(), name='horimeter_create'),
    path('update/<str:machine>&<str:name>', update_horimeter_per_machine_and_name, name='update_horimeter_per_machine_and_name')
]