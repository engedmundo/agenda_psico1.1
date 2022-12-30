from apps.patient_management.models import Patient
from apps.patient_management.tests.fixtures import patient_fixture
from django.test import TestCase


class PatientModelTest(TestCase):
    def test_create_patient(self):
        patient = patient_fixture()
        self.assertIsInstance(patient, Patient)
