from apps.core.models import Psychologist
from apps.core.tests.fixtures import psychologist_fixture
from apps.financial_management.models import PaymentPlain
from faker import Faker

faker = Faker("pt_BR")


def payment_plain_fixture(
    psychologist: Psychologist = None,
    name_plain=faker.word(),
    plain_value=faker.random_int(min=0, max=500),
) -> PaymentPlain:

    if psychologist is None:
        psychologist = psychologist_fixture()

    return PaymentPlain.objects.create(
        psychologist=psychologist,
        name_plain=name_plain,
        plain_value=plain_value,
    )
