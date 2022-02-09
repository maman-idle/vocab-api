from pathlib import Path
import os, dj_database_url
from decouple import config


""" Cloudinary starts below here, install cloudinary and Pillow using pip to start managing your dynamic
files, and then import cloudinary to setup the configuration.Next step is including the cloudinary 
inside the installed apps in the settings.py"""
import cloudinary

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config("SECRET_KEY")
SECRET_KEY = os.getenv('SECRET_KEY', 'yes') #for heroku


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Cloudinary storage, just for image storage. We don't want to override the staticfiles config,
    # so we put the cloudinary apps UNDER the staticfiles apps. 
    'cloudinary_storage',
    'cloudinary',

    #DRF
    'rest_framework',
    'rest_framework.authtoken',

    'accounts',
    'words',

    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vocab_api.urls'

AUTH_USER_MODEL = "accounts.Account"

# CORS
CORS_ORIGIN_ALLOW_ALL = True

#Cloudinary Config.
#The Cloudinary general config (project scope), I use .env file to store the sensitive data and access
# it using decouple library. You NEED to manually setup the env variables in Heroku if you want to 
# use decouple because the git won't upload the .env files.
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config("CLOUD_NAME"),
    'API_KEY': config("API_KEY"),
    'API_SECRET': config("API_SECRET")
}

#configuration for importing cloudinary directly into your python package/class.
cloudinary.config(
    cloud_name = config("CLOUD_NAME"),
    api_key = config("API_KEY"),
    api_secret = config("API_SECRET")
)

#File upload handler, use it to handle file uploaded into a temporary file location.
# Important for checking file size befor uploading to Cloudinary.
# Check the image validation inside models.py. 
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

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

WSGI_APPLICATION = 'vocab_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
   ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/staticfiles')
#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Dynamic Media using Cloudinary Storage, the media url tells Cloudinary to create 'media' folder,
# inside your Cloudinary account. That will be the main directory for storing files for your Cloudinary
# in this project. You can designate the sub-folder by using 'upload_to' parameter inside the models.py.
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)


""" LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
 """