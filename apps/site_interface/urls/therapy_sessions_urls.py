from django.urls import path

from ..views import (
    pacient_sessions,
    pacient_session_delete,
    pacient_session_delete_confirm,
    pacient_session_register,
    pacient_session_register_save,
    pacient_session_search,
    pacient_session_update,
    pacient_sessions_details,
)

app_name = 'pacient_sessions'


urlpatterns = [
    path(
        '',
        pacient_sessions,
        name='pacient_sessions',
    ),
    path(
        '<int:id>',
        pacient_sessions_details,
        name='pacient_sessions_details',
    ),
    path(
        'register',
        pacient_session_register,
        name='pacient_session_register',
    ),
    path(
        'create',
        pacient_session_register_save,
        name='pacient_session_register_save',
    ),
    path(
        'update/<int:id>',
        pacient_session_update,
        name='pacient_session_update',
    ),
    path(
        'delete/<int:id>',
        pacient_session_delete,
        name='pacient_session_delete',
    ),
    path(
        'delete/<int:id>/confirm',
        pacient_session_delete_confirm,
        name='pacient_session_delete_confirm',
    ),
    path(
        'search/',
        # pacient_session_delete_confirm,
        pacient_session_search,
        name='search_pacient_session',
    ),
]
