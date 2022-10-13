import pytest
from apps.core.factories.psychologist_factory import PsychologistFactory
from apps.financial_management.models.payment_control import PaymentControl
from apps.financial_management.models.payment_plain import PaymentPlain
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_create_payment_plain(payment_plain_fixture):
    _test.assertIsInstance(payment_plain_fixture, PaymentPlain)


@pytest.mark.models
def test_create_payment_control(payment_control_fixture):
    _test.assertIsInstance(payment_control_fixture, PaymentControl)
