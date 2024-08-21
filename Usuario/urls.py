from django.urls import path
from Usuario import views


urlpatterns = [
    path('auto/', views.emailUser, name="auto_usuarios"),
    path('createUser', views.usuario_auto, name='create_users'),
]