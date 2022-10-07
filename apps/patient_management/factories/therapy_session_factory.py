import factory
from apps.patient_management.factories.patient_factory import PatientFactory
from apps.patient_management.models import TherapySession
from faker import Faker

fake = Faker("pt_BR")


class TherapySessionFactory(factory.django.DjangoModelFactory):
    patient = factory.SubFactory(PatientFactory)
    session_id = fake.random_int(min=1, max=100)
    patient = factory.SubFactory(PatientFactory)
    date_session = fake.date()
    hour_session = fake.time()
    fault = False
    justify_fault = fake.paragraph()
    evolution = fake.paragraph()
    forwarding = fake.paragraph()
    payment = False

    class Meta:
        model = TherapySession
