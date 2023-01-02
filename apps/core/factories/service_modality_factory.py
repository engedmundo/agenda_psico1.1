import factory
from apps.core.models import ServiceModalitiy
from faker import Faker

from .psychologist_factory import PsychologistFactory

faker = Faker("pt_BR")


class ServiceModalityFactory(factory.django.DjangoModelFactory):
    psychologist = factory.SubFactory(PsychologistFactory)
    name = faker.word()
    description = faker.paragraph(nb_sentences=5)

    class Meta:
        model = ServiceModalitiy
