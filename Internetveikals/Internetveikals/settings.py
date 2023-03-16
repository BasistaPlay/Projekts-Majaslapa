

"""
Django settings for Internetveikals project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from django.contrib.messages import constants as message_constants
from django.utils.translation import gettext_lazy as _
from msilib.schema import Media
from pathlib import Path
import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w1z&-=gbzj-n4gr31hmk@6!nj8^s^1(@pk=yq&%^p(-dhg)0a3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ["https://2e7a-212-142-81-248.eu.ngrok.io"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django_cleanup.apps.CleanupConfig',
    'modeltranslation',
    'django.contrib.admin',
    'mptt',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reset_migrations',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'cart',
    'crispy_forms',
    'majaslapa.apps.UsersConfig',
    "django_admin_lightweight_date_hierarchy",
]
SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'Internetveikals.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'cart.context_processor.cart_total_amount',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Internetveikals',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'lv'
USE_I18N = True
USE_L10N = True

TIME_ZONE = 'GMT'

USE_I18N = True
USE_L10N = True
USE_TZ = True


LOCALE_PATHS = (
    os.path.join(os.path.dirname(__file__), "locale"),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

if DEBUG:

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

else:

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


# E-pasta pievienošana
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'baltictechh@gmail.com'
EMAIL_HOST_PASSWORD = 'qzuuduwbnktnlhkc'


# Lokalizētās valodas
def gettext(s): return s


LANGUAGES = (
    ('lv', gettext('Latvian')),
    ('en', gettext('English'))
)

PARLER_LANGUAGES = {
    None: (
        {'code': 'lv', },  # Latvian
        {'code': 'en', },  # English
    ),
    'default': {
        'fallbacks': ['lv'],
        'hide_untranslated': False,
    }
}

MODELTRANSLATION_DEFAULT_LANGUAGE = 'lv'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'


# Admin lapas konfigurācija
JAZZMIN_SETTINGS = {
    "site_title": "Admins",
    "site_header": "Admins lapa",
    "site_brand": "Admin",
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "language_chooser": True
}

# groza configs
CART_SESSION_ID = 'cart'


# stripe konfigurācija
APPEND_SLASH = False
STRIPE_PUBLISHABLE_KEY = 'pk_test_51M5VxtAiAB9ovPLga1k2eSAWMRn7F6vw40FGkloEscteVnlNmD1zOILAnCpgdroNDXRWFuhNiDtpOPu7z8ffVZzo00QZVw6MIz'
STRIPE_SECRET_KEY = 'sk_test_51M5VxtAiAB9ovPLgA2df0XbLinZBiwnZwVCF3rOfGBVMgInrqZZzIiIRXs5SGYBpvFQ6yqInTGWu9KTziIV49Ue100b3VTJZTE'
STRIPE_ENDPOINT_SECRET = 'whsec_3968e39f8d852940ae08b12da5496411298768c227beb093cd8d68075fd33bc7'


MESSAGE_LEVEL = message_constants.DEBUG
