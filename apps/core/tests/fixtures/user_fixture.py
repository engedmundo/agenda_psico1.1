import pytest
from apps.core.factories.user_factory import UserFactory


@pytest.fixture
def user_fixture(db):
    return UserFactory()
