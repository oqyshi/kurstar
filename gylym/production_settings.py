import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'MPETs2E7r9xox6ivgo4WlTwY7gAjAeQa9GVVwXL2HOVX98t4QngXZXvDhjm67yZG'

DEBUG = False
ALLOWED_HOSTS = ['89.108.65.97', '2a00:f940:2:4:2::16d4', '89-108-65-97.cloudvps.regruhosting.ru', 'kurstar.kz']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_project_db',
        'USER': 'django',
        'PASSWORD': 'Aivae7ahRaro',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST_USER = 'kurstar.help@gmail.com'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_PASSWORD = 'Qqwerty1!'
