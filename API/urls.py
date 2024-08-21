from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from Usuario import urls as users_urls
from Horimetros import urls as horimeter_urls
from Alarmes import urls as alarmes_urls
from Producao import urls as prod_urls


urlpatterns = [

    path('admin/', admin.site.urls),

    # TOKEN DE ACESSO DA API
    path('api_token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # URLS DOS HORIMETROS DA API
    path('api_horimeter/', include(horimeter_urls)),
    path('api_horimeter/', include(horimeter_urls)),

    # URLS DOS ALARMES DA API
    path('api_alarmes/', include(alarmes_urls)),

    path("api_producao/", include(prod_urls)),

    path('home/', include(users_urls))
]
