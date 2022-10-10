from django.urls import path

from . import views

app_name = 'site_interface'


urlpatterns = [
    path(
        '',
        views.home,
        name='home',
    ),
    path(
        'login',
        views.login_view,
        name='login_view',
    ),
    path(
        'login/create',
        views.login_create,
        name='login_create',
    ),
    path(
        'logout',
        views.logout_view,
        name='logout_view',
    ),
]

