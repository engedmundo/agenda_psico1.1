import pytest
from django.contrib.auth.models import User
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_create_user(make_user):
    _test.assertIsInstance(make_user, User)
