import pytest
from apps.core.factories import PsychologistFactory


@pytest.fixture
def make_psychologist(db):
    return PsychologistFactory()
