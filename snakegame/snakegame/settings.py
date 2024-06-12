import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-qd)k2p=n0&zk65=c236w5n8puhr(+gj1l33-i&efhip%t-lg79')

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'game',  # Replace with your actual app name if different
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

ROOT_URLCONF = 'snakegame.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template engine to use
        'DIRS': [os.path.join(BASE_DIR, '../frontend/build')],  # List of directories where Django will look for templates
        'APP_DIRS': True,  # Whether to look for templates inside installed applications
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Provides `debug` context variable
                'django.template.context_processors.request',  # Provides `request` context variable
                'django.contrib.auth.context_processors.auth',  # Provides `user` and `perms` context variables
                'django.contrib.messages.context_processors.messages',  # Provides `messages` context variable
            ],
        },
    },
]


WSGI_APPLICATION = 'snakegame.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../frontend/build/static'),
]


# CORS Settings
CORS_ALLOW_ALL_ORIGINS = False

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom settings for production
if not DEBUG:
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
    CORS_ALLOWED_ORIGINS = ['http://yourdomain.com', 'https://yourdomain.com']
