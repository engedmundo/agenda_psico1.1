# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
import os

DATABASES = {
    "default": {
        "ENGINE": os.environ.get(
            "DATABASE_ENGINE", default="django.db.backends.sqlite3"
        ),
        "NAME": os.environ.get("DATABASE_NAME", default="./db.sqlite3"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
    }
}
