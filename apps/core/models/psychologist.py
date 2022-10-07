from django.db import models
from .common_info import CommonInfo
from django.contrib.auth.models import User



class Psychologist(CommonInfo):
    psychologist = models.ForeignKey(
        User,
        verbose_name="Psicólogo(a)",
        on_delete=models.SET_NULL,
        null=True,
    )
    crp_register = models.CharField(
        "Registro CRP",
        max_length=20
    )
    professional_address = models.CharField(
        "Endereço Profissional",
        max_length=200
    )
    secondary_address = models.CharField(
        "Endereço secundário",
        max_length=200,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        "Telefone",
        max_length=15
    )
    cpf = models.CharField(
        'CPF',
        null=True,
        blank=True,
        max_length=11
    )

    class Meta:
        verbose_name = "Psicólogo"
        verbose_name_plural = "Psicólogos"

    def __str__(self):
        return self.psychologist
