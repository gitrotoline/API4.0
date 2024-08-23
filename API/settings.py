import os
from datetime import timedelta
from pathlib import Path
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w*v^y5uu%x8=**9qorpl8a!slr6q8xi*bdjp61_duducb23u$)'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', True)
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'Horimetros',
    "Usuario",
    "Alarmes",
    "Producao",
    "Receitas",
    "Timeline",
    "Temperatura",
    "Corrente",
    "Rwtc",
    "Sensor",
    "Velocidade",
    "Status"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'API.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'API.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'teste_new_api',
        'USER': 'RotoAPI',
        'PASSWORD': '6D&W!E3p7dNvAjM',
        'HOST': 'localhost',
        'PORT': 3333,
    },
    'TESTE': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'TESTE',
        'USER': 'RotoAPI',
        'PASSWORD': '6D&W!E3p7dNvAjM',
        'HOST': 'localhost',
        'PORT': 3333,
    },
    'M442': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'M442',
        'USER': 'RotoAPI',
        'PASSWORD': '6D&W!E3p7dNvAjM',
        'HOST': 'localhost',
        'PORT': 3333,
    },
    'M365': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'M365',
        'USER': 'RotoAPI',
        'PASSWORD': '6D&W!E3p7dNvAjM',
        'HOST': 'localhost',
        'PORT': 3333,
    },
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "support@rotoline.com"
EMAIL_HOST_PASSWORD = "5780nhe<5Zo*"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
TIME_INPUT_FORMATS = ['%H:%M', ]

LANGUAGES = (
    ('es', _('Espanhol')),
    ('en', _('English')),
    ('pt-BR', _('Português')),
)

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = "UTC"
USE_TZ = True
USE_I18N = True
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# Static
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'
#
# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'home2'
# LOGOUT_REDIRECT_URL = 'login'


# Configurações do Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# Configurações do Simple JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=36500),  # Aproximadamente 100 anos
    'REFRESH_TOKEN_LIFETIME': timedelta(days=0),  # Imediatamente expirado
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Adicione a configuração DEFAULT_AUTO_FIELD para apontar para BigAutoField
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
