import factory
from apps.patient_management.factories import ProntuaryFactory
from apps.patient_management.models import TherapySession
from faker import Faker

faker = Faker("pt_BR")


class TherapySessionFactory(factory.django.DjangoModelFactory):
    prontuary = factory.SubFactory(ProntuaryFactory)
    session_number = faker.random_int(min=0, max=500)
    date_session = faker.date_object()
    hour_session = faker.time_object()
    fault = False
    justify_fault = faker.sentence(nb_words=10)
    evolution = faker.paragraph(nb_sentences=5)
    forwarding = faker.paragraph(nb_sentences=5)
    payment = False

    class Meta:
        model = TherapySession
