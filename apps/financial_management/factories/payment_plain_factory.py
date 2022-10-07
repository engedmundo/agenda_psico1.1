import factory
from apps.core.factories.psychologist_factory import PsychologistFactory
from apps.financial_management.models import PaymentPlain
from faker import Faker

fake = Faker("pt_BR")


class PaymentPlainFactory(factory.django.DjangoModelFactory):
    psycologist = factory.SubFactory(PsychologistFactory)
    name_plain = fake.word()
    plain_value = fake.numerify(text="R$ ###,##")

    class Meta:
        model = PaymentPlain
