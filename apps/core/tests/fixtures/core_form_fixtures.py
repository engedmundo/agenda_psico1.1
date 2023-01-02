from .user_fixture import user_fixture
from faker import Faker

faker = Faker("pt_BR")


class CoreFormFixtures:
    def make_login_form_data(self):
        _user = user_fixture()
        return {
            "username": _user.username,
            "password": _user.password,
        }
