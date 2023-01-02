from apps.core.models import Psychologist
from apps.core.tests.fixtures.psychologist_fixture import make_psychologist
from apps.financial_management.models import PaymentPlain
from apps.financial_management.tests.fixtures.payment_plain_fixture import (
    make_payment_plain,
)
from apps.patient_management.models import Patient
from faker import Faker

faker = Faker("pt_BR")


def make_patient(
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
        psychologist = make_psychologist()

    if plain is None:
        plain = make_payment_plain(
            psychologist=psychologist,
        )

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
