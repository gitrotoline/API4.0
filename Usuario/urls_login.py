from django.urls import path
from Usuario import views

urlpatterns = [
    path("vUser/", views.validate_user, name="validate_user"),
    path("vAccount/<str:user>", views.validate_password, name="validate_password"),
    path("vLogin", views.login_in_system, name="login_in_system")

]