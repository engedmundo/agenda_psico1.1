import factory
from apps.core.models import Psychologist
from faker import Faker

from .user_factory import UserFactory

faker = Faker("pt_BR")


class PsychologistFactory(factory.django.DjangoModelFactory):
    psychologist = factory.SubFactory(UserFactory)
    crp_register = faker.numerify(text="CRP 0#/######-IS")
    short_description = faker.sentence(nb_words=5)
    professional_address = faker.address()
    city = faker.city()
    secondary_address = faker.address()
    phone_number = faker.phone_number()
    cpf = faker.cpf()
    instagram_link = faker.uri()
    twitter_link = faker.uri()
    linkedin_link = faker.uri()
    whatsapp_number = faker.phone_number()
    bio = faker.paragraph(nb_sentences=5)
    schedule_description = faker.paragraph(nb_sentences=5)

    class Meta:
        model = Psychologist
