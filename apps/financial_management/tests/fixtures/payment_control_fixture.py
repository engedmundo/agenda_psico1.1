from apps.financial_management.models import (
    PaymentControl,
)
from apps.patient_management.models import Prontuary
from apps.patient_management.tests.fixtures import prontuary_fixture
from faker import Faker

faker = Faker("pt_BR")


def payment_control_fixture(
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
) -> PaymentControl:

    if prontuary is None:
        prontuary = prontuary_fixture()

    return PaymentControl.objects.create(
        prontuary=prontuary,
        value_paid=value_paid,
        date_of_pay=date_of_pay,
        description=description,
        payment_method=payment_method,
    )
