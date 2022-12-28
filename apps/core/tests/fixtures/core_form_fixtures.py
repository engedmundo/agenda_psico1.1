from .core_models_fixtures import CoreModelFixtures
from faker import Faker

faker = Faker("pt_BR")


class CoreFormFixtures:
    def make_login_form_data(self):
        _user = CoreModelFixtures().make_user()
        return {
            "username": _user.username,
            "password": _user.password,
        }
