from django.test import TestCase
from apps.core.tests.fixtures.core_models_fixtures import CoreModelFixtures
from django.contrib.auth.models import User


class UserModelTest(TestCase, CoreModelFixtures):
    def test_create_user(self):
        _user = self.make_user()
        self.assertIsInstance(_user, User)
