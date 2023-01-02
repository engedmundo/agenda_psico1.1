import factory
from apps.core.factories import PsychologistFactory
from apps.financial_management.models import PaymentPlain
from faker import Faker

faker = Faker("pt_BR")


class PaymentPlainFactory(factory.django.DjangoModelFactory):
    psychologist = factory.SubFactory(PsychologistFactory)
    name_plain = faker.word()
    plain_value = faker.random_int(min=0, max=500)

    class Meta:
        model = PaymentPlain
