from apps.patient_management.tests.fixtures.prontuary_fixture import make_prontuary
from apps.financial_management.models import PaymentPlain
from apps.financial_management.tests.fixtures import *
from apps.patient_management.models import Patient, Prontuary, TherapySession
from faker import Faker

faker = Faker("pt_BR")


def therapy_session_fixture(
    prontuary: Prontuary = None,
    session_number=faker.random_int(min=0, max=500),
    date_session=faker.date_object(),
    hour_session=faker.time_object(),
    evolution=faker.paragraph(nb_sentences=5),
    forwarding=faker.paragraph(nb_sentences=5),
) -> TherapySession:

    if prontuary is None:
        prontuary = make_prontuary()

    return TherapySession.objects.create(
        prontuary=prontuary,
        session_number=session_number,
        date_session=date_session,
        hour_session=hour_session,
        evolution=evolution,
        forwarding=forwarding,
    )
