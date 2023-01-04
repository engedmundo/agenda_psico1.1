import pytest
from apps.financial_management.factories import PaymentPlainFactory
from apps.patient_management.factories import PatientFactory


@pytest.fixture
def make_patient(db):
    payment_plain = PaymentPlainFactory()
    return PatientFactory(
        plain=payment_plain,
        psychologist=payment_plain.psychologist,
    )
