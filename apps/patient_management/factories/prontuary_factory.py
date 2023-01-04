import factory
from apps.core.factories import ServiceModalityFactory
from apps.patient_management.factories import PatientFactory
from apps.patient_management.models import Prontuary
from faker import Faker

faker = Faker("pt_BR")


class ProntuaryFactory(factory.django.DjangoModelFactory):
    patient = factory.SubFactory(PatientFactory)
    type_of_service = factory.SubFactory(ServiceModalityFactory)
    prontuary_number = faker.random_int(min=0, max=500)
    open_date = faker.date_object()
    close_date = faker.date_object()
    demand_description = faker.paragraph(nb_sentences=5)

    class Meta:
        model = Prontuary
