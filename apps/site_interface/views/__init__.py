from .home_views import home, login_create, login_view, logout_view
from .patient_views import (
    patient_delete,
    patient_delete_confirm,
    patient_details,
    patient_register,
    patient_register_save,
    patient_update,
    patients,
)
from .payment_control_views import (
    payment_delete,
    payment_delete_confirm,
    payment_details,
    payment_register,
    payment_register_save,
    payment_update,
    payments,
)
from .payment_plain_views import (
    plains,
    plains_register,
    plains_register_save,
    plains_update,
    plains_delete_confirm,
    plains_delete,
)
from .prontuary_views import (
    prontuaries,
    prontuary_details,
    prontuary_register,
    prontuary_register_save,
    prontuary_update,
    prontuary_delete_confirm,
    prontuary_delete,
)
from .therapy_session_views import (
    pacient_sessions,
    pacient_session_delete,
    pacient_session_delete_confirm,
    pacient_session_register,
    pacient_session_register_save,
    pacient_session_search,
    pacient_session_update,
    pacient_sessions_details,
)
