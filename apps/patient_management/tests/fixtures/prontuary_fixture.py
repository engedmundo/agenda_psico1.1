import pytest
from apps.core.factories import ServiceModalityFactory
from apps.financial_management.factories import PaymentPlainFactory
from apps.patient_management.factories import PatientFactory, ProntuaryFactory
from faker import Faker

faker = Faker("pt_BR")


@pytest.fixture
def make_prontuary(db):
    payment_plain = PaymentPlainFactory()
    psycho = payment_plain.psychologist
    service = ServiceModalityFactory(
        psychologist=psycho,
    )
    patient = PatientFactory(
        psychologist=psycho,
        plain=payment_plain,
    )
    return ProntuaryFactory(
        patient=patient,
        type_of_service=service,
    )
