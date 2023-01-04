import pytest
from apps.patient_management.models import Patient
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_create_patient(make_patient):
    _test.assertIsInstance(make_patient, Patient)
