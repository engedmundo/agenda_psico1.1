import factory
from django.contrib.auth.models import User
from faker import Faker

fake = Faker("pt_BR")


class UserFactory(factory.django.DjangoModelFactory):
    username = fake.user_name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    is_staff = False
    is_active = True
    is_superuser = False

    class Meta:
        model = User
