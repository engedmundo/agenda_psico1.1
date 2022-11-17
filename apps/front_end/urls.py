from django.urls import path

from .views import *

# home views
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
]

# payment plains urls
urlpatterns += [
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
]

# patients urls
urlpatterns += [
    path(
        "patients/",
        patients_list,
        name="patients_list",
    ),
    path(
        "patients/create/",
        create_patient,
        name="create_patient",
    ),
    path(
        "patients/save/",
        patient_save,
        name="patient_save",
    ),
    path(
        "patients/<int:id>/update/",
        patient_update,
        name="patient_update",
    ),
    path(
        "patient/<int:id>/archive/",
        patient_archive,
        name="patient_archive",
    ),
    path(
        "patient/<int:id>/archive_confirm/",
        patient_archive_confirm,
        name="patient_archive_confirm",
    ),
    path(
        "patients/archived/",
        patients_archived,
        name="patients_arquived",
    ),
    path(
        "patient/<int:id>/unarchive/",
        patient_unarchive,
        name="patient_unarchive",
    ),
    # path(
    #     "patients/<int:id>/delete/",
    #     patients_delete,
    #     name="patients_delete",
    # ),
    # path(
    #     "patients/<int:id>/delete_confirm/",
    #     patients_delete_confirm,
    #     name="patients_delete_confirm",
    # ),
]
