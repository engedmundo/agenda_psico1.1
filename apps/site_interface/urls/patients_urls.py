from django.urls import path

from ..views import (
    patient_delete,
    patient_delete_confirm,
    patient_details,
    patient_register,
    patient_register_save,
    patient_update,
    patients,
)

app_name = "patients"


urlpatterns = [
    path(
        "",
        patients,
        name="pacients",
    ),
    path(
        "<int:id>",
        patient_details,
        name="pacient_details",
    ),
    path(
        "register",
        patient_register,
        name="pacient_register",
    ),
    path(
        "register/save",
        patient_register_save,
        name="pacient_register_save",
    ),
    path(
        "update/<int:id>",
        patient_update,
        name="pacient_update",
    ),
    path(
        "delete/<int:id>",
        patient_delete,
        name="pacient_delete",
    ),
    path(
        "delete/<int:id>/confirm",
        patient_delete_confirm,
        name="pacient_delete_confirm",
    ),
]
