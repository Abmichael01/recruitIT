from pathlib import Path
import os
from dotenv import load_dotenv
import django_heroku
import dj_database_url

load_dotenv()




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fk_bp*7x@d%97mgz+46%c#4@_gq0osh9-z*=j@j%3qg8(358er'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["recruitit-47654d4acc27.herokuapp.com", "127.0.0.1", "localhost"]



# Application definition

INSTALLED_APPS = [
    # custom admin app
    "jazzmin",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    
    

    # use email as username apps
    'django_use_email_as_username.apps.DjangoUseEmailAsUsernameConfig',
    'custom_user.apps.CustomUserConfig',

    #django google sso
    "django_google_sso",
    

    # installed apps
    "authenticate",
    "recruitment",
    "profiles",

]

# custom user model
AUTH_USER_MODEL = 'custom_user.User'

LOGIN_URL = '/authenticate/login'


# google sso configs
GOOGLE_SSO_CLIENT_ID = os.getenv('GOOGLE_SSO_CLIENT_ID')
GOOGLE_SSO_PROJECT_ID = os.getenv('GOOGLE_SSO_PROJECT_ID')
GOOGLE_SSO_CLIENT_SECRET = os.getenv('GOOGLE_SSO_CLIENT_SECRET')

GOOGLE_SSO_ALLOWABLE_DOMAINS = ["gmail.com"]
GOOGLE_SSO_ENABLED = True

GOOGLE_SSO_LOGO_URL = "images/logo.png"

GOOGLE_SSO_TEXT = "Continue with Google"

GOOGLE_SSO_PRE_LOGIN_CALLBACK = "authenticate.hooks.pre_login_user"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    
    
]

ROOT_URLCONF = 'recruitIT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'recruitment.context_processors.notifications',
            ],
        },
    },
]

WSGI_APPLICATION = 'recruitIT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': os.getenv("DATABSE_NAME"),
    #     'USER': os.getenv("DATABSE_USER"),
    #     'PASSWORD': os.getenv("DATABSE_PASSWORD"),
    #     'HOST': os.getenv("DATABSE_HOST"),
    #     'PORT': os.getenv("DATABSE_PORT"),       
    # }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())

# Email Config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'recruit.it000@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

JAZZMIN_SETTINGS = {
    "site_header": "RecruitIT",
    "site_brand": "RecruitIT: IT Placement gets easier",
    "site_logo": "images/logo.png",
    "copyright": "recruitit.site",
}

