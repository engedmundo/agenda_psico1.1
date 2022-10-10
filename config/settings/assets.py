import os

from .environment import BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, "static"),
    # os.path.join(BASE_DIR, "base_static"),
# )
