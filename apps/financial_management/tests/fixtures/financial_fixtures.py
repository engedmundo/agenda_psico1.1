from apps.core.models import Psychologist
from apps.core.tests.fixtures import psychologist_fixture
from apps.financial_management.models import (
    ExpenseCategory,
    ExpenseControl,
    PaymentControl,
    PaymentPlain,
)
from apps.financial_management.tests.fixtures import expense_category_fixture
from apps.patient_management.models import Prontuary
from apps.patient_management.tests.fixtures import prontuary_fixture
from faker import Faker

faker = Faker("pt_BR")


def payment_plain_fixture(
    psychologist: Psychologist = None,
    name_plain=faker.word(),
    plain_value=faker.random_int(min=0, max=500),
) -> PaymentPlain:

    if psychologist is None:
        psychologist = psychologist_fixture()

    return PaymentPlain.objects.create(
        psychologist=psychologist,
        name_plain=name_plain,
        plain_value=plain_value,
    )


def payment_control_fixture(
    prontuary: Prontuary = None,
    value_paid=faker.random_int(min=0, max=500),
    date_of_pay=faker.date_object(),
    description=faker.paragraph(nb_sentences=5),
    payment_method=faker.random_element(
        elements=(
            "Pix",
            "Dinheiro",
            "Tranferência",
            "Cheque",
        ),
    ),
) -> PaymentControl:

    if prontuary is None:
        prontuary = prontuary_fixture()

    return PaymentControl.objects.create(
        prontuary=prontuary,
        value_paid=value_paid,
        date_of_pay=date_of_pay,
        description=description,
        payment_method=payment_method,
    )


def expense_category_fixture(
    psychologist: Psychologist = None,
    name=faker.word(),
    description=faker.paragraph(nb_sentences=5),
) -> ExpenseCategory:

    if psychologist is None:
        psychologist = psychologist_fixture()

    return ExpenseCategory.objects.create(
        psychologist=psychologist,
        name=name,
        description=description,
    )


def expense_control_fixture(
    psychologist: Psychologist = None,
    category: ExpenseCategory = None,
    expense_value=faker.random_int(min=0, max=500),
    completion_date=faker.date_object(),
    description=faker.paragraph(nb_sentences=5),
    cpf_cnpj=faker.cpf(),
) -> ExpenseControl:

    if psychologist is None:
        psychologist = psychologist_fixture()

    if category is None:
        category = expense_category_fixture()

    return ExpenseControl.objects.create(
        psychologist=psychologist,
        category=category,
        expense_value=expense_value,
        completion_date=completion_date,
        description=description,
        cpf_cnpj=cpf_cnpj,
    )
