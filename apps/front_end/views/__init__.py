from .home_views import (
    home,
    login_create,
    login_view,
    logout_view,
    professional_description,
)
from .patient_views import (
    create_patient,
    patient_archive,
    patient_archive_confirm,
    patient_save,
    patient_update,
    patients_archived,
    patients_list,
    patient_unarchive,
    patient_delete,
    patient_delete_confirm,
)
from .payment_plains_views import (
    create_payment_plain,
    payment_plain_archive,
    payment_plain_archive_confirm,
    payment_plain_delete,
    payment_plain_delete_confirm,
    payment_plain_save,
    payment_plain_unarchive,
    payment_plain_update,
    payment_plains_archived,
    payment_plains_list,
)
from .prontuary_views import prontuaries_list
from .profile_views import my_profile, my_profile_update
