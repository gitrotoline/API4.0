from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt import views as jwt_views

from Usuario import urls as users_urls
from Horimetros import urls as horimeter_urls
from Alarmes import urls as alarmes_urls
from Producao import urls as prod_urls
from Receitas import urls as recipes_urls, urls_recipe_data as recipe_data_urls
from Timeline import urls as timeline_urls, urls_timeline_clp as timeline_clp_urls
from Temperatura import urls as temp_urls
from Corrente import urls as amps_urls
from Rwtc import urls as rwtc_urls
from Sensor import urls as sensor_urls
from Usuario.views import CustomTokenObtainView
from Velocidade import urls as speed_urls
from Status import urls as status_machine
from Usuario import views as view_pro_users
from Usuario import urls_login

urlpatterns = [
    # URL Translate
    path('i18n/', include('django.conf.urls.i18n')),

    # LOGIN AND REGISTER USERS
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', include(urls_login)),
    path('validate_username/', view_pro_users.validate_username, name='validate_username'),
    path('register', login_required(view_pro_users.register), name='register'),

    # URL Documentation
    path('documentation', view_pro_users.documentation, name="documentation"),

    # HOME AND DOCUMENTATION API
    path('home/', include(users_urls)),
    path('admin_secret_karaio_adivinha_ai_otario_renigth_fora_plmr_de_Dios/', admin.site.urls),

    # TOKEN DE ACESSO DA API
    path('api_token/', CustomTokenObtainView.as_view(), name='token_obtain'),

    # URLS DOS HORIMETROS DA API
    path('api_horimeter/<str:machine>/', include(horimeter_urls)),

    # URLS DOS ALARMES DA API
    path('api_alarmes/<str:machine>/', include(alarmes_urls)),

    # URLS DADOS DA PRODUCAO (RELATORIO RESUMIDO)
    path("api_producao/<str:machine>/", include(prod_urls)),

    # URLS DAS RECEITAS E  # URLS DAS RECEITAS DADOS
    path("api_receitas/<str:machine>/", include(recipes_urls)),
    path("api_receitas_dados/<str:machine>/", include(recipe_data_urls)),

    # URLS DA TIMELINE
    path("api_timeline/<str:machine>/", include(timeline_urls)),
    path("api_timeline_sensor/<str:machine>/", include(timeline_clp_urls)),

    # URLS DA TEMPERATURA
    path("api_temperature/<str:machine>/", include(temp_urls)),
    path('api_eletric_amps/<str:machine>/', include(amps_urls)),
    path('api_rwtc/<str:machine>/', include(rwtc_urls)),

    # URLS SENSORES
    path("api_sensor/<str:machine>/", include(sensor_urls)),

    # URL DE VELOCIDADE
    path('api_speed/<str:machine>/', include(speed_urls)),

    # URL QUE MOSTRA STATUS DA MAQUINA
    path('api_status/<str:machine>/', include(status_machine)),

]

handler404 = 'Usuario.views.handler404'
# handler500 = 'Usuario.views.handler500'
