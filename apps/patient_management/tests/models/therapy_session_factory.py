import pytest
from apps.patient_management.models import TherapySession
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_therapy_session(therapy_session_fixture):
    _test.assertIsInstance(therapy_session_fixture, TherapySession)
