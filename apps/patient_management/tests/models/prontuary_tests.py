import pytest
from apps.patient_management.models import Prontuary
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_create_prontuary(make_prontuary):
    _test.assertIsInstance(make_prontuary, Prontuary)
