import pytest
from apps.patient_management.factories.patient_factory import PatientFactory
from apps.patient_management.factories.prontuary_factory import ProntuaryFactory
from apps.patient_management.factories.therapy_session_factory import (
    TherapySessionFactory,
)


@pytest.fixture
def patient_fixture(db):
    return PatientFactory()


@pytest.fixture
def prontuary_fixture(db):
    return ProntuaryFactory()


@pytest.fixture
def therapy_session_fixture(db):
    return TherapySessionFactory()
