import pytest
from apps.core.factories import ServiceModalityFactory


@pytest.fixture
def make_service_modality(db):
    return ServiceModalityFactory()
