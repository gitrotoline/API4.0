from django.urls import path
from Timeline.views import list_timeline, TimelineCreate, TimelineDadosCreate, list_timeline_dados


urlpatterns = [
    path('<date_min>&<date_max>', list_timeline, name='list_timeline'),
    path('create', TimelineCreate.as_view(), name='create_timeline'),
    path('dados/<int:id_ciclo>', list_timeline_dados, name='list_timeline_dados'),
    path('dados/create', TimelineDadosCreate.as_view(), name='timelinedados_create'),
]