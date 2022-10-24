from django.urls import path

from .views import (home, login_create, login_view, logout_view, my_profile,
                    my_profile_update, professional_description)

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
        "my_profile",
        my_profile_update,
        name="my_profile",
    ),
]
