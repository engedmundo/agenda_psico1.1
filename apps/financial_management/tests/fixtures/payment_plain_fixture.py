from apps.core.models import Psychologist
from apps.core.tests.fixtures.psychologist_fixture import make_psychologist
from apps.financial_management.models import PaymentPlain
from faker import Faker

faker = Faker("pt_BR")


def make_payment_plain(
    psychologist: Psychologist = None,
    name_plain=faker.word(),
    plain_value=faker.random_int(min=0, max=500),
) -> PaymentPlain:

    if psychologist is None:
        psychologist = make_psychologist()

    return PaymentPlain.objects.create(
        psychologist=psychologist,
        name_plain=name_plain,
        plain_value=plain_value,
    )
