import pytest
from apps.core.factories import UserFactory


@pytest.fixture
def make_user(db):
    return UserFactory()
