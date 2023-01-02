import pytest
from apps.financial_management.factories import PaymentPlainFactory


@pytest.fixture
def make_payment_plain(db):
    return PaymentPlainFactory()
