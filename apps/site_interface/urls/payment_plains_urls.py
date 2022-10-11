from django.urls import path

from ..views import (
    plains,
    plains_register,
    plains_register_save,
    plains_update,
    plains_delete_confirm,
    plains_delete,
)

app_name = 'plains'

urlpatterns = [

    path(
        '', 
        plains,
        name='plains',
    ),
    path(
        'register', 
        plains_register,
        name='plains_register',
    ),
    path(
        'register/save', 
        plains_register_save,
        name='plains_register_save',
    ),
    path(
        '<int:id>', 
        plains_update,
        name='plains_update',
    ),
    path(
        'delete/<int:id>', 
        plains_delete,
        name='plains_delete',
    ),
    path(
        'delete/<int:id>/confirm', 
        plains_delete_confirm,
        name='plains_delete_confirm',
    ),    
]
