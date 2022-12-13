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
    path(
        "patient/<int:id>/delete/",
        patient_delete,
        name="patient_delete",
    ),
    path(
        "patient/<int:id>/delete_confirm/",
        patient_delete_confirm,
        name="patient_delete_confirm",
    ),
]

# prontuaries urls
urlpatterns += [
    path(
        "prontuaries/",
        prontuaries_list,
        name="prontuaries_list",
    ),
    path(
        "prontuaries/create/",
        create_prontuary,
        name="create_prontuary",
    ),
    path(
        "prontuaries/save/",
        prontuary_save,
        name="prontuary_save",
    ),
    path(
        "prontuaries/<int:id>/update/",
        prontuary_update,
        name="prontuary_update",
    ),
    path(
        "prontuary/<int:id>/",
        prontuary_details,
        name="prontuary_details",
    ),
    path(
        "prontuary/<int:id>/archive/",
        prontuary_archive,
        name="prontuary_archive",
    ),
    path(
        "prontuary/<int:id>/archive_confirm/",
        prontuary_archive_confirm,
        name="prontuary_archive_confirm",
    ),
    path(
        "prontuaries/archived/",
        prontuaries_archived,
        name="prontuaries_arquived",
    ),
    path(
        "prontuary/<int:id>/unarchive/",
        prontuary_unarchive,
        name="prontuary_unarchive",
    ),
    path(
        "prontuary/<int:id>/delete/",
        prontuary_delete,
        name="prontuary_delete",
    ),
    path(
        "prontuary/<int:id>/delete_confirm/",
        prontuary_delete_confirm,
        name="prontuary_delete_confirm",
    ),
]

# therapy sessions urls
urlpatterns += [
    path(
        "prontuaries/<int:id>/create_session/",
        create_therapy_session,
        name="create_session",
    ),
    path(
        "prontuaries/<int:id>/create_session/save/",
        therapy_session_save,
        name="therapy_session_save",
    ),
    path(
        "therapy_session/<int:id>/update/",
        therapy_session_update,
        name="therapy_session_update",
    ),
    path(
        "therapy_session/<int:id>/update_payment/",
        therapy_session_update_payment,
        name="therapy_session_update_payment",
    ),
    path(
        "therapy_session/<int:id>/update_fault/",
        therapy_session_update_fault,
        name="therapy_session_update_fault",
    ),
    # path(
    #     "prontuary/<int:id>/delete/",
    #     prontuary_delete,
    #     name="prontuary_delete",
    # ),
    # path(
    #     "prontuary/<int:id>/delete_confirm/",
    #     prontuary_delete_confirm,
    #     name="prontuary_delete_confirm",
    # ),
]
