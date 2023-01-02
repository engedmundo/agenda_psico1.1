from apps.core.models import ServiceModalitiy
from apps.core.tests.fixtures import make_service_modality
from apps.patient_management.models import Patient, Prontuary
from apps.patient_management.tests.fixtures.patient_fixture import make_patient
from faker import Faker

faker = Faker("pt_BR")


def make_prontuary(
    patient: Patient = None,
    type_of_service: ServiceModalitiy = None,
    prontuary_number=faker.random_int(min=0, max=500),
    open_date=faker.date_object(),
    close_date=faker.date_object(),
    demand_description=faker.paragraph(nb_sentences=5),
) -> Prontuary:

    if patient is None:
        patient = make_patient()

    if type_of_service is None:
        type_of_service = make_service_modality(
            psychologist=patient.psychologist,
        )

    return Prontuary.objects.create(
        patient=patient,
        prontuary_number=prontuary_number,
        open_date=open_date,
        close_date=close_date,
        demand_description=demand_description,
        type_of_service=type_of_service,
    )
