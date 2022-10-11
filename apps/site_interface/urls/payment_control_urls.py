from django.urls import path

from ..views import (
    payment_delete,
    payment_delete_confirm,
    payment_details,
    payment_register,
    payment_register_save,
    payment_update,
    payments,
)

app_name = 'payment_control'

urlpatterns = [
    path(
        '',
        payments,
        name='payments',
    ),
    path(
        'register',
        payment_register,
        name='payment_register',
    ),
    path(
        'register/save',
        payment_register_save,
        name='payment_register_save',
    ),
    path(
        '<int:id>',
        payment_update,
        name='payment_update',
    ),
    path(
        'delete/<int:id>',
        payment_delete,
        name='payment_delete',
    ),
    path(
        'delete/<int:id>/confirm',
        payment_delete_confirm,
        name='payment_delete_confirm',
    ),
]
