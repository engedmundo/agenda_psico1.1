from django.urls import path

from ..views import (
    prontuaries,
    prontuary_details,
    prontuary_register,
    prontuary_register_save,
    prontuary_update,
    prontuary_delete_confirm,
    prontuary_delete,
)

app_name = 'prontuaries'

urlpatterns = [
    path('',
        prontuaries,
        name='prontuaries',
    ),
    path('<int:id>',
        prontuary_details,
        name='prontuary_details',
    ),
    path('register',
        prontuary_register,
        name='prontuary_register',
    ),
    path('register/save',
        prontuary_register_save,
        name='prontuary_register_save',
    ),
    path('update/<int:id>',
        prontuary_update,
        name='prontuary_update',
    ),
    path('delete/<int:id>',
        prontuary_delete,
        name='prontuary_delete',
    ),
    path('delete/<int:id>/confirm',
        prontuary_delete_confirm,
        name='prontuary_delete_confirm',
    ),
]
