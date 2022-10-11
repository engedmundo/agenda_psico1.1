from django.urls import path, include

from ..views import home, login_create, login_view, logout_view

app_name = "site_interface"


urlpatterns = [
    path(
        "",
        home,
        name="home",
    ),
    path(
        "login",
        login_view,
        name="login_view",
    ),
    path(
        "login/create",
        login_create,
        name="login_create",
    ),
    path(
        "logout",
        logout_view,
        name="logout_view",
    ),
]
