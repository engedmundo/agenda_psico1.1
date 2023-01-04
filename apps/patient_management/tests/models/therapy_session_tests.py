import pytest
from apps.patient_management.models import TherapySession
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_create_therapy_session(make_therapy_session):
    _test.assertIsInstance(make_therapy_session, TherapySession)
