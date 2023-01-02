import factory
from django.contrib.auth.models import User
from faker import Faker

faker = Faker("pt_BR")


class UserFactory(factory.django.DjangoModelFactory):
    username = faker.user_name()
    first_name = faker.first_name()
    last_name = faker.last_name()
    password = faker.password()
    email = faker.email()
    is_staff = False
    is_active = True
    is_superuser = False

    class Meta:
        model = User
