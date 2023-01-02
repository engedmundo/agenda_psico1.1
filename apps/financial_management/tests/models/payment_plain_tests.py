from django.test import TestCase
from apps.financial_management.tests.fixtures import make_payment_plain
from apps.financial_management.models import PaymentPlain


class PaymentPlainModelTest(TestCase):
    def test_create_payment_plain(self):
        payment_plain = make_payment_plain()
        self.assertIsInstance(payment_plain, PaymentPlain)
