from django.test import TestCase
from apps.core.tests.fixtures import *
from apps.core.models import Psychologist


class PsychologistModelTest(TestCase):
    def test_create_psychologist(self):
        _user = psychologist_fixture()
        self.assertIsInstance(_user, Psychologist)
