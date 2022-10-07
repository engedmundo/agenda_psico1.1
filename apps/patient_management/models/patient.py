from apps.core.models import CommonInfo, Psychologist
from apps.financial_management.models import PaymentPlain
from django.db import models


# Create your models here.
class Patient(CommonInfo):
    pacient_name = models.CharField(
        "Nome Completo",
        max_length=100
    )
    psychologist = models.ForeignKey(
        Psychologist,
        verbose_name="Profissional responsável",
        on_delete=models.SET_NULL,
        null=True
    )
    birth_date = models.DateField(
        "Data de Nascimento",
        null=True,
        blank=True
    )
    cpf = models.CharField(
        "CPF",
        null=True,
        blank=True,
        max_length=11
    )
    phone_number = models.CharField(
        "Telefone",
        max_length=15
    )
    pacient_address = models.CharField(
        "Endereço",
        null=True,
        blank=True,
        max_length=100
    )
    email = models.EmailField(
        "E-mail",
        null=True,
        blank=True,
        max_length=100
    )
    occupation = models.CharField(
        "Profissão",
        null=True,
        blank=True,
        max_length=100
    )
    responsable = models.CharField(
        "Responsavel",
        null=True,
        blank=True,
        max_length=100
    )
    fone_resp = models.CharField(
        "Telefone responsavel",
        null=True,
        blank=True,
        max_length=15
    )
    session_week_day = models.CharField(
        "Dia das sessões",
        null=True,
        blank=True,
        max_length=15
    )
    session_hour = models.CharField(
        "Hora das sessões",
        null=True,
        blank=True,
        max_length=15
    )
    plain = models.ForeignKey(
        PaymentPlain,
        verbose_name="Plano",
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.pacient_name
