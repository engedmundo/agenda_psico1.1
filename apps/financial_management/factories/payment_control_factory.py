import factory
from apps.financial_management.models import PaymentControl
from apps.patient_management.factories.patient_factory import PatientFactory
from apps.patient_management.factories.therapy_session_factory import (
    TherapySessionFactory,
)
from faker import Faker

fake = Faker("pt_BR")


class PaymentControlFactory(factory.django.DjangoModelFactory):
    pacient = factory.SubFactory(PatientFactory)
    value_pay = fake.numerify(text="R$ ###,##")
    data_pay = fake.date()
    description = fake.random_element(
        elements=(
            "Pix",
            "Dinheiro",
            "Tranferência",
            "Cheque",
        )
    )
    way_pay = fake.phone_number()
    therapy_sessions = factory.SubFactory(TherapySessionFactory)

    class Meta:
        model = PaymentControl
