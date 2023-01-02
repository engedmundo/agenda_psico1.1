import pytest
from apps.core.models import Psychologist
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_create_psychologist(make_psychologist):
    _test.assertIsInstance(make_psychologist, Psychologist)
