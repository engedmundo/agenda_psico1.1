from apps.patient_management.models import Prontuary
from apps.patient_management.tests.fixtures.prontuary_fixture import make_prontuary
from django.test import TestCase


class ProntuaryModelTest(TestCase):
    def test_create_prontuary(self):
        prontuary = make_prontuary()
        self.assertIsInstance(prontuary, Prontuary)
