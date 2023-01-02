import pytest
from apps.core.models import ServiceModalitiy
from django.test import TestCase

_test = TestCase()


@pytest.mark.models
def test_create_service_modality(make_service_modality):
    _test.assertIsInstance(make_service_modality, ServiceModalitiy)
