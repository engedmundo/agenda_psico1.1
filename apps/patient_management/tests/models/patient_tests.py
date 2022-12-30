from apps.core.tests.fixtures import psychologist_fixture
from apps.financial_management.tests.fixtures import payment_plain_fixture
from apps.patient_management.models import Patient
from apps.patient_management.tests.fixtures import patient_fixture
from django.test import TestCase


class PatientModelTest(TestCase):
    def test_create_patient(self):
        psychologist = psychologist_fixture()
        payment_plain = payment_plain_fixture(
            psychologist=psychologist,
        )
        patient = patient_fixture(
            psychologist=psychologist,
            plain=payment_plain,
        )
        self.assertIsInstance(patient, Patient)
