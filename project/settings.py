import os
from environs import Env

env = Env()
env.read_env()
site_secret_key = env('SITE_SECRET_KEY')
bd_password = env('BD_PASSWORD')
bd_path = env('BD_PATH')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': bd_path,
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': bd_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = site_secret_key

DEBUG = env.bool("DEBUG")

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
