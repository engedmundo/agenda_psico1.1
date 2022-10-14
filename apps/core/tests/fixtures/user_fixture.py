import pytest
from apps.core.factories.psychologist_factory import PsychologistFactory
from apps.core.factories.user_factory import UserFactory


@pytest.fixture
def user_fixture(db):
    return UserFactory()


@pytest.fixture
def psychologist_fixture(db):
    return PsychologistFactory()
