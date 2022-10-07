import pytest
from apps.core.models.psychologist import Psychologist
from django.contrib.auth.models import User


@pytest.mark.models
def test_create_user(user_fixture):
    assert isinstance(user_fixture, User)


@pytest.mark.models
def test_create_psycologist(psychologist_fixture):
    assert isinstance(psychologist_fixture, Psychologist)
