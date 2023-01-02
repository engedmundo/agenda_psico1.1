import pytest
from apps.financial_management.models import PaymentPlain
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_create_payment_plain(make_payment_plain):
    _test.assertIsInstance(make_payment_plain, PaymentPlain)
