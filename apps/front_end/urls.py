from django.urls import path

from .views import *

urlpatterns = [
    path(
        "",
        home,
        name="home",
    ),
    path(
        "professional_description/<int:id>/",
        professional_description,
        name="professional_description",
    ),
    path(
        "login/",
        login_view,
        name="login",
    ),
    path(
        "login/create/",
        login_create,
        name="login_create",
    ),
    path(
        "logout/",
        logout_view,
        name="logout",
    ),
    path(
        "my_profile/",
        my_profile_update,
        name="my_profile",
    ),
    path(
        "payment_plains/",
        payment_plains_list,
        name="payment_plains",
    ),
    path(
        "payment_plains/create/",
        create_payment_plain,
        name="create_payment_plain",
    ),
    path(
        "payment_plains/save/",
        payment_plain_save,
        name="payment_plain_save",
    ),
    path(
        "payment_plain/<int:id>/update/",
        payment_plain_update,
        name="payment_plain_update",
    ),
    path(
        "payment_plain/<int:id>/archive/",
        payment_plain_archive,
        name="payment_plain_archive",
    ),
    path(
        "payment_plain/<int:id>/archive_confirm/",
        payment_plain_archive_confirm,
        name="payment_plain_archive_confirm",
    ),
    path(
        "payment_plains/archived/",
        payment_plains_archived,
        name="payment_plains_arquived",
    ),
    path(
        "payment_plain/<int:id>/unarchive/",
        payment_plain_unarchive,
        name="payment_plain_unarchive",
    ),
    path(
        "payment_plain/<int:id>/delete/",
        payment_plain_delete,
        name="payment_plain_delete",
    ),
    path(
        "payment_plain/<int:id>/delete_confirm/",
        payment_plain_delete_confirm,
        name="payment_plain_delete_confirm",
    ),
    path(
        "patients/",
        patients_list,
        name="patients_list",
    ),
    # path(
    #     "payment_plains/create/",
    #     create_payment_plain,
    #     name="create_payment_plain",
    # ),
    # path(
    #     "payment_plains/save/",
    #     payment_plain_save,
    #     name="payment_plain_save",
    # ),
    # path(
    #     "payment_plain/<int:id>/update/",
    #     payment_plain_update,
    #     name="payment_plain_update",
    # ),
    # path(
    #     "payment_plain/<int:id>/archive/",
    #     payment_plain_archive,
    #     name="payment_plain_archive",
    # ),
    # path(
    #     "payment_plain/<int:id>/archive_confirm/",
    #     payment_plain_archive_confirm,
    #     name="payment_plain_archive_confirm",
    # ),
    # path(
    #     "payment_plains/archived/",
    #     payment_plains_archived,
    #     name="payment_plains_arquived",
    # ),
    # path(
    #     "payment_plain/<int:id>/unarchive/",
    #     payment_plain_unarchive,
    #     name="payment_plain_unarchive",
    # ),
    # path(
    #     "payment_plain/<int:id>/delete/",
    #     payment_plain_delete,
    #     name="payment_plain_delete",
    # ),
    # path(
    #     "payment_plain/<int:id>/delete_confirm/",
    #     payment_plain_delete_confirm,
    #     name="payment_plain_delete_confirm",
    # ),
]
