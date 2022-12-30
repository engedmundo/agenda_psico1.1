from django.test import TestCase
from apps.core.tests.fixtures import service_modality_fixture
from apps.core.models import ServiceModalitiy


class ServiceModalityModelTest(TestCase):
    def test_create_service_modality(self):
        _user = service_modality_fixture()
        self.assertIsInstance(_user, ServiceModalitiy)
