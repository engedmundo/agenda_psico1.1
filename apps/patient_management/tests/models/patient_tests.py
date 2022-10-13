import pytest
from apps.patient_management.models import Patient
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_patient(patient_fixture):
    _test.assertIsInstance(patient_fixture, Patient)
