from django.test import TestCase
from apps.core.tests.fixtures.core_models_fixtures import CoreModelFixtures
from apps.core.models import ServiceModalitiy


class ServiceModalityModelTest(TestCase, CoreModelFixtures):
    def test_create_service_modality(self):
        _user = self.make_service_modality()
        self.assertIsInstance(_user, ServiceModalitiy)
