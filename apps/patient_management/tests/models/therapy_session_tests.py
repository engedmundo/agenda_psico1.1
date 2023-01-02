from apps.patient_management.models import TherapySession
from apps.patient_management.tests.fixtures.therapy_session_fixture import (
    therapy_session_fixture,
)
from django.test import TestCase


class TherapySessionModelTest(TestCase):
    def test_create_therapy_session(self):
        session = therapy_session_fixture()
        self.assertIsInstance(session, TherapySession)
