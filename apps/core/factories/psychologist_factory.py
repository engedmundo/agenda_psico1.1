import json

import factory
from apps.core.factories.user_factory import UserFactory
from apps.core.models.psychologist import Psychologist
from faker import Faker

fake = Faker("pt_BR")


class PsychologistFactory(factory.django.DjangoModelFactory):
    psychologist = factory.SubFactory(UserFactory)
    crp_register = fake.numerify(text="CRP 0#/######-IS")
    professional_address = fake.address()
    secondary_address = fake.address()
    phone_number = fake.phone_number()
    cpf = fake.date()

    class Meta:
        model = Psychologist
