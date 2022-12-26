import factory
from apps.core.factories.psychologist_factory import PsychologistFactory
from apps.financial_management.factories.payment_plain_factory import (
    PaymentPlainFactory,
)
from apps.patient_management.models import Patient
from faker import Faker

fake = Faker("pt_BR")
# _psychologist = PsychologistFactory()

class PatientFactory(factory.django.DjangoModelFactory):
    patient_name = fake.name()
    # psychologist = _psychologist
    birth_date = fake.date()
    cpf = fake.cpf()
    phone_number = fake.phone_number()
    patient_address = fake.address()
    email = fake.email()
    occupation = fake.job()
    responsable = fake.name()
    phone_resp = fake.phone_number()
    session_week_day = fake.day_of_week()
    session_hour = fake.numerify(text="##:##")
    # plain = factory.SubFactory(PaymentPlainFactory)

    class Meta:
        model = Patient
