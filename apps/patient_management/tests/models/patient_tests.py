from apps.patient_management.models import Patient
from apps.patient_management.tests.fixtures.patient_fixture import make_patient
from django.test import TestCase


class PatientModelTest(TestCase):
    def test_create_patient(self):
        patient = make_patient()
        self.assertIsInstance(patient, Patient)
