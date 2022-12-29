from django.test import TestCase
from apps.core.tests.fixtures import *
from django.contrib.auth.models import User


class UserModelTest(TestCase):
    def test_create_user(self):
        _user = user_fixture()
        self.assertIsInstance(_user, User)
