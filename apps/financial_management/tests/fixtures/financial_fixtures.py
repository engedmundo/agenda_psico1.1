from apps.core.models import Psychologist
from apps.core.tests.fixtures.core_models_fixtures import CoreModelFixtures
from apps.patient_management.tests.fixtures.patient_fixtures import (
    PatientManagementModelFixtures,
)
from apps.financial_management.models import (
    ExpenseCategory,
    ExpenseControl,
    PaymentPlain,
)
from faker import Faker

faker = Faker("pt_BR")


class FinancialManagementModelFixtures:
    def __init__(self) -> None:
        self.core_models_fixtures = CoreModelFixtures()
        self.patient_models_fixtures = PatientManagementModelFixtures()

    def payment_plain_fixture(
        self,
        psychologist: Psychologist = None,
        name_plain=faker.word(),
        plain_value=faker.random_int(min=0, max=500),
    ) -> PaymentPlain:

        if psychologist is None:
            psychologist = self.core_models_fixtures.psychologist_fixture()

        return PaymentPlain.objects.create(
            psychologist=psychologist,
            name_plain=name_plain,
            plain_value=plain_value,
        )

    def payment_control_fixture(
        self,
        psychologist: Psychologist = None,
        name_plain=faker.word(),
        plain_value=faker.random_int(min=0, max=500),
    ) -> PaymentPlain:

        if psychologist is None:
            psychologist = self.psychologist

        return PaymentPlain.objects.create(
            psychologist=psychologist,
            name_plain=name_plain,
            plain_value=plain_value,
        )

    def expense_category_fixture(
        self,
        psychologist: Psychologist = None,
        name=faker.word(),
        description=faker.paragraph(nb_sentences=5),
    ) -> ExpenseCategory:

        if psychologist is None:
            psychologist = self.core_models_fixtures.psychologist_fixture()

        return ExpenseCategory.objects.create(
            psychologist=psychologist,
            name=name,
            description=description,
        )

    def expense_control_fixture(
        self,
        psychologist: Psychologist = None,
        category: ExpenseCategory = None,
        expense_value=faker.random_int(min=0, max=500),
        completion_date=faker.date_object(),
        description=faker.paragraph(nb_sentences=5),
        cpf_cnpj=faker.cpf(),
    ) -> ExpenseControl:

        if psychologist is None:
            psychologist = self.core_models_fixtures.psychologist_fixture()

        if category is None:
            category = self.expense_category_fixture()

        return ExpenseControl.objects.create(
            psychologist=psychologist,
            category=category,
            expense_value=expense_value,
            completion_date=completion_date,
            description=description,
            cpf_cnpj=cpf_cnpj,
        )
