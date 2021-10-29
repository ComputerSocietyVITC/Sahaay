from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
AUTHOR = "ComputerSociety - VIT Chennai"

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "Logic.apps.LogicConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "multiselectfield",
    "django_neomodel",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Core.urls"

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

ASGI_APPLICATION = "Core.asgi.application"


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

AUTH_USER_MODEL = "Logic.UserModel"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Calcutta"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
MOUNT_DATABASE = False
MOUNT_DJANGO = False
PSQL = False
CACHING_AND_BACKUP = False
GRAPH = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "Database/db.sql",
    }
}


if MOUNT_DATABASE != True:
    DATABASES.update({
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "Database/db.sqlite3",
        }
    })
if PSQL == True:
    DATABASES.update({
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postges",
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "HOST": "Testing",
            "PORT": 5432,
        }
    })

if GRAPH:
    NEOMODEL_NEO4J_BOLT_URL = os.environ.get('NEO4J_BOLT_URL','bolt://username:password@localhost:7687')
    NEOMODEL_SIGNALS = True
    NEOMODEL_FORCE_TIMEZONE = False
    NEOMODEL_ENCRYPTED_CONNECTION = True
    NEOMODEL_MAX_POOL_SIZE = 50

if CACHING_AND_BACKUP:
    DATABASES.update({
        "cassandra": {
            "ENGINE": "django_cassandra_engine",
            "NAME": "test",
            "TEST_NAME": "djassandra",
            "USER": "cassandra",
            "PASSWORD": "cassandra",
            "HOST": "localhost",
            "PORT": "9042",
            "OPTIONS": {
                "replication": {
                    "strategy_class": "SimpleStrategy",
                    "replication_factor": 1,
                }
            },
        }
    })


