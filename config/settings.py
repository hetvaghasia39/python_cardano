"""
    settings file for cardano boilerplate implementaion of python using drf
"""

import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read("config.ini")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-#h1z%43@$n-87$^gkk53n^sav6xwc=a#4i4##wftcz93n8^fsa"

DEBUG = True

ALLOWED_HOSTS = []


BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "apps.users",
]

INSTALLED_APPS = BASE_APPS + CUSTOM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_USER_MODEL = "users.CardanoUser"

DATABASE_CREDENTIAL = config["DATABASE"]
DATABASES = {
    "default": {
        "ENGINE": DATABASE_CREDENTIAL["DB_ENGINE"],
        "NAME": DATABASE_CREDENTIAL["DB_NAME"],
        "USER": DATABASE_CREDENTIAL["DB_USER"],
        "PASSWORD": DATABASE_CREDENTIAL.get("DB_PASSWORD"),
        "HOST": DATABASE_CREDENTIAL["DB_ENDPOINT"],
        "PORT": DATABASE_CREDENTIAL["DB_PORT"],
        # 'ATOMIC_REQUESTS': True,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
