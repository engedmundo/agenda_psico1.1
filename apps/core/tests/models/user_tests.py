import pytest
from apps.core.models.psychologist import Psychologist
from django.contrib.auth.models import User
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_create_user(user_fixture):
    _test.assertIsInstance(user_fixture, User)


@pytest.mark.models
def test_create_psycologist(psychologist_fixture):
    _test.assertIsInstance(psychologist_fixture, Psychologist)
