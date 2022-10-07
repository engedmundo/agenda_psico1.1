import pytest


from apps.core.models.psychologist import Psychologist
from django.contrib.auth.models import User


@pytest.mark.models
def test_create_user(user_fixture):
    print(user_fixture)
    assert isinstance(user_fixture, User)