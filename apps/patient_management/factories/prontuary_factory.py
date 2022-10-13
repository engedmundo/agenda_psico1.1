import factory
from apps.patient_management.factories.patient_factory import PatientFactory
from apps.patient_management.models import Prontuary
from faker import Faker

fake = Faker("pt_BR")


class ProntuaryFactory(factory.django.DjangoModelFactory):
    patient = factory.SubFactory(PatientFactory)
    open_date = fake.date()
    demand_description = fake.paragraph()

    class Meta:
        model = Prontuary
