from django.test import TestCase
from apps.financial_management.tests.fixtures import payment_control_fixture
from apps.financial_management.models import PaymentControl


class PaymentControlModelTest(TestCase):
    def test_create_payment_control(self):
        payment_control = payment_control_fixture()
        self.assertIsInstance(payment_control, PaymentControl)
