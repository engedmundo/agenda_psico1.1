from apps.core.tests.fixtures import psychologist_fixture, service_modality_fixture
from apps.financial_management.tests.fixtures import payment_plain_fixture
from apps.patient_management.models import Prontuary
from apps.patient_management.tests.fixtures import patient_fixture, prontuary_fixture
from django.test import TestCase


class ProntuaryModelTest(TestCase):
    def test_create_prontuary(self):
        psychologist = psychologist_fixture()
        service_modality = service_modality_fixture(
            psychologist=psychologist,
        )
        payment_plain = payment_plain_fixture(
            psychologist=psychologist,
        )
        patient = patient_fixture(
            psychologist=psychologist,
            plain=payment_plain,
        )
        prontuary = prontuary_fixture(
            patient=patient,
            type_of_service=service_modality,
        )
        self.assertIsInstance(prontuary, Prontuary)
