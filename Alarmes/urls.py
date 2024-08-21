from django.urls import path
from Alarmes.views import list_alarmes, alarmes_create


urlpatterns = [
    path('<date_min>&<date_max>', list_alarmes, name='list_alarmes'),
    path('create', alarmes_create, name='create_alarmes')
]