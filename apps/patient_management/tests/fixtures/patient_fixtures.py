from apps.core.models import Psychologist, ServiceModalitiy
from apps.core.tests.fixtures import *
from apps.financial_management.models import PaymentPlain
from apps.financial_management.tests.fixtures import *
from apps.patient_management.models import Patient, Prontuary, TherapySession
from faker import Faker

faker = Faker("pt_BR")


def patient_fixture(
    patient_name=faker.name(),
    psychologist: Psychologist = None,
    plain: PaymentPlain = None,
    birth_date=faker.date_of_birth(),
    cpf=faker.cpf(),
    phone_number=faker.phone_number(),
    patient_address=faker.address(),
    email=faker.email(),
    occupation=faker.word(),
    school=faker.company(),
    responsable=faker.name(),
    phone_resp=faker.phone_number(),
    father=faker.name_male(),
    phone_father=faker.phone_number(),
    mother=faker.name_female(),
    phone_mother=faker.phone_number(),
    session_week_day=faker.day_of_week(),
    session_hour=faker.time_object(),
    session_value=faker.random_int(min=0, max=500),
    discount_agreement=faker.words(nb=5),
) -> Patient:

    if psychologist is None:
        psychologist = psychologist_fixture()

    if plain is None:
        plain = payment_plain_fixture()

    return Patient.objects.create(
        patient_name=patient_name,
        psychologist=psychologist,
        plain=plain,
        birth_date=birth_date,
        cpf=cpf,
        phone_number=phone_number,
        patient_address=patient_address,
        email=email,
        occupation=occupation,
        school=school,
        responsable=responsable,
        phone_resp=phone_resp,
        father=father,
        phone_father=phone_father,
        mother=mother,
        phone_mother=phone_mother,
        session_week_day=session_week_day,
        session_hour=session_hour,
        session_value=session_value,
        discount_agreement=discount_agreement,
    )


def prontuary_fixture(
    patient: Patient = None,
    prontuary_number=faker.random_int(min=0, max=500),
    open_date=faker.date_object(),
    close_date=faker.date_object(),
    demand_description=faker.paragraph(nb_sentences=5),
    type_of_service: ServiceModalitiy = None,
) -> Prontuary:

    if patient is None:
        patient = patient_fixture()

    if type_of_service is None:
        type_of_service = service_modality_fixture()

    return Prontuary.objects.create(
        patient=patient,
        prontuary_number=prontuary_number,
        open_date=open_date,
        close_date=close_date,
        demand_description=demand_description,
        type_of_service=type_of_service,
    )


def therapy_session_fixture(
    self,
    # ver aqui
    prontuary: Prontuary = None,
    value_paid=faker.random_int(min=0, max=500),
    date_of_pay=faker.date_object(),
    description=faker.paragraph(nb_sentences=5),
    payment_method=faker.random_element(
        elements=(
            "Pix",
            "Dinheiro",
            "Tranferência",
            "Cheque",
        ),
    ),
) -> TherapySession:

    if prontuary is None:
        prontuary = self.prontuary_fixture()

    return TherapySession.objects.create(
        prontuary=prontuary,
        value_paid=value_paid,
        date_of_pay=date_of_pay,
        description=description,
        payment_method=payment_method,
    )
