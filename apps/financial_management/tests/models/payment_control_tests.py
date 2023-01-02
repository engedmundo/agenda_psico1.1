from django.test import TestCase
from apps.financial_management.tests.fixtures import make_payment_control
from apps.financial_management.models import PaymentControl


class PaymentControlModelTest(TestCase):
    def test_create_payment_control(self):
        payment_control = make_payment_control()
        self.assertIsInstance(payment_control, PaymentControl)
