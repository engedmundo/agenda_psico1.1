from apps.core.models import Psychologist, ServiceModalitiy
from apps.core.tests.fixtures import *
from apps.financial_management.models import PaymentPlain
from apps.financial_management.tests.fixtures import *
from apps.patient_management.models import Patient, Prontuary, TherapySession
from faker import Faker

faker = Faker("pt_BR")


def therapy_session_fixture(
    self,
    # ver aqui
    prontuary: Prontuary = None,
    value_paid=faker.random_int(min=0, max=500),
    date_of_pay=faker.date_object(),
    description=faker.paragraph(nb_sentences=5),
    payment_method=faker.random_element(
        elements=(
            "Pix",
            "Dinheiro",
            "Tranferência",
            "Cheque",
        ),
    ),
) -> TherapySession:

    if prontuary is None:
        prontuary = self.prontuary_fixture()

    return TherapySession.objects.create(
        prontuary=prontuary,
        value_paid=value_paid,
        date_of_pay=date_of_pay,
        description=description,
        payment_method=payment_method,
    )
