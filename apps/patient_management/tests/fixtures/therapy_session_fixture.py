import pytest
from apps.patient_management.factories import TherapySessionFactory
from apps.financial_management.factories import PaymentPlainFactory
from apps.core.factories import ServiceModalityFactory
from apps.patient_management.factories import PatientFactory, ProntuaryFactory


@pytest.fixture
def make_therapy_session(db):
    payment_plain = PaymentPlainFactory()
    psycho = payment_plain.psychologist
    service = ServiceModalityFactory(
        psychologist=psycho,
    )
    patient = PatientFactory(
        psychologist=psycho,
        plain=payment_plain,
    )
    prontuary = ProntuaryFactory(
        patient=patient,
        type_of_service=service,
    )
    return TherapySessionFactory(
        prontuary=prontuary,
    )
