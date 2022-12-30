from django.contrib.auth.models import User
from faker import Faker

faker = Faker("pt_BR")


def user_fixture(
    username=faker.user_name(),
    first_name=faker.first_name(),
    last_name=faker.last_name(),
    password=faker.password(),
    email=faker.email(),
    is_staff=False,
    is_active=True,
    is_superuser=False,
) -> User:
    return User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password,
        email=email,
        is_staff=is_staff,
        is_active=is_active,
        is_superuser=is_superuser,
    )
