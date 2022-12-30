from apps.core.models import Psychologist, ServiceModalitiy
from faker import Faker

from .psychologist_fixture import psychologist_fixture

faker = Faker("pt_BR")


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
