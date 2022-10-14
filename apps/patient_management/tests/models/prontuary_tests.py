import pytest
from apps.patient_management.models import Prontuary, TherapySession
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_prontuary(prontuary_fixture):
    _test.assertIsInstance(prontuary_fixture, Prontuary)
