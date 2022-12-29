from django.test import TestCase
from apps.financial_management.tests.fixtures import *
from apps.financial_management.models import PaymentPlain


class PaymentPlainModelTest(TestCase):
    def test_create_payment_plain(self):
        payment_plain = payment_plain_fixture()
        self.assertIsInstance(payment_plain, PaymentPlain)
