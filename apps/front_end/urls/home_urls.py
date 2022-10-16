from django.urls import path

from ..views import home

app_name = "site_interface"


urlpatterns = [
    path(
        "",
        home,
        name="home",
    ),
]
