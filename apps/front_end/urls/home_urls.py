from django.urls import path

from ..views import (
    home,
    login_create,
    login_view,
    logout_view,
    professional_description,
    my_profile,
)

app_name = "site_interface"


urlpatterns = [
    path(
        "",
        home,
        name="home",
    ),
    path(
        "professional_description/<int:id>",
        professional_description,
        name="professional_description",
    ),
    path(
        "login",
        login_view,
        name="login",
    ),
    path(
        "login/create",
        login_create,
        name="login_create",
    ),
    path(
        "logout",
        logout_view,
        name="logout",
    ),
    path(
        "my_profile/<int:id>",
        my_profile,
        name="my_profile",
    ),
]
