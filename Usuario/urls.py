from django.contrib.auth.decorators import login_required
from django.urls import path
from Usuario import views


urlpatterns = [
    path('', login_required(views.index), name="home"),
    path('token_access', views.token_access, name="token_access"),
    path('auto/', views.email_user, name="auto_usuarios"),
    path('createUser', views.usuario_auto, name='create_users'),
]