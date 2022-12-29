from apps.core.models import Psychologist, ServiceModalitiy
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

def psychologist_fixture(
    _user: User = None,
    crp_register=faker.numerify(text="CRP 0#/######-IS"),
    short_description=faker.sentence(nb_words=5),
    professional_address=faker.address(),
    city=faker.city(),
    secondary_address=faker.address(),
    phone_number=faker.phone_number(),
    cpf=faker.date(),
    instagram_link=faker.uri(),
    twitter_link=faker.uri(),
    linkedin_link=faker.uri(),
    whatsapp_number=faker.phone_number(),
    bio=faker.paragraph(nb_sentences=5),
    schedule_description=faker.paragraph(nb_sentences=5),
) -> Psychologist:

    if _user is None:
        _user = user_fixture()

    return Psychologist.objects.create(
        psychologist=_user,
        crp_register=crp_register,
        short_description=short_description,
        professional_address=professional_address,
        city=city,
        secondary_address=secondary_address,
        phone_number=phone_number,
        cpf=cpf,
        instagram_link=instagram_link,
        twitter_link=twitter_link,
        linkedin_link=linkedin_link,
        whatsapp_number=whatsapp_number,
        bio=bio,
        schedule_description=schedule_description,
    )

def service_modality_fixture(
    psychologist: Psychologist = None,
    name=faker.word(),
    description=faker.paragraph(nb_sentences=5),
) -> ServiceModalitiy:

    if psychologist is None:
        psychologist = psychologist_fixture()

    return ServiceModalitiy.objects.create(
        psychologist=psychologist,
        name=name,
        description=description,
    )
