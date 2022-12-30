from apps.patient_management.models import Prontuary
from apps.patient_management.tests.fixtures import prontuary_fixture
from django.test import TestCase


class ProntuaryModelTest(TestCase):
    def test_create_prontuary(self):
        prontuary = prontuary_fixture()
        self.assertIsInstance(prontuary, Prontuary)
