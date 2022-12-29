from django.test import TestCase
from apps.core.tests.fixtures.core_models_fixtures import CoreModelFixtures
from apps.core.models import Psychologist


class PsychologistModelTest(TestCase, CoreModelFixtures):
    def test_create_psychologist(self):
        _user = self.psychologist_fixture()
        self.assertIsInstance(_user, Psychologist)
