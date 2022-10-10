import pytest
from apps.financial_management.factories.payment_control_factory import (
    PaymentControlFactory,
)
from apps.financial_management.factories.payment_plain_factory import (
    PaymentPlainFactory,
)


@pytest.fixture
def payment_control_fixture(db):
    return PaymentControlFactory()


@pytest.fixture
def payment_plain_fixture(db):
    return PaymentPlainFactory()
