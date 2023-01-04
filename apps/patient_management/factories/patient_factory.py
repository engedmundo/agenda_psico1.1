import factory
from apps.core.factories import PsychologistFactory
from apps.financial_management.factories import PaymentPlainFactory
from apps.patient_management.models import Patient
from faker import Faker

faker = Faker("pt_BR")


class PatientFactory(factory.django.DjangoModelFactory):
    patient_name = faker.name()
    psychologist = factory.SubFactory(PsychologistFactory)
    plain = factory.SubFactory(PaymentPlainFactory)
    birth_date = faker.date_of_birth()
    cpf = faker.cpf()
    phone_number = faker.phone_number()
    patient_address = faker.address()
    email = faker.email()
    occupation = faker.word()
    school = faker.company()
    responsable = faker.name()
    phone_resp = faker.phone_number()
    father = faker.name_male()
    phone_father = faker.phone_number()
    mother = faker.name_female()
    phone_mother = faker.phone_number()
    session_week_day = faker.day_of_week()
    session_hour = faker.time_object()
    session_value = faker.random_int(min=0, max=500)
    discount_agreement = faker.words(nb=5)

    class Meta:
        model = Patient
