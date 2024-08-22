from django.urls import path
from Timeline.views import TimelineDados_sensoresCreate, list_timeline_sensores

urlpatterns = [
    path('<date_min>&<date_max>', list_timeline_sensores, name='list_timeline_sensor'),
    path('create', TimelineDados_sensoresCreate.as_view(), name='create_timeline'),
]