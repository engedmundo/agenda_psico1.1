# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
from .environment import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# for use postgres
# DATABASES = {
#         'default': {
#             'ENGINE': env('DB_ENGINE'),
#             'NAME': env('DB_NAME'),
#             'USER': env('DB_USER'),
#             'PASSWORD': env('DB_PASSWORD'),
#             'HOST': env('DB_HOST'),
#             'PORT': env('DB_PORT'),
#         }
#     }