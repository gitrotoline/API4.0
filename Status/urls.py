from django.urls import path
from Status.views import status_machine_view, Status_update

urlpatterns = [

    path('', status_machine_view, name='status_machine'),
    path('update/<int:pk>', Status_update.as_view(), name='update_status_machine'),

]