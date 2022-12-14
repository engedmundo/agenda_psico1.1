from django.contrib.auth.models import User
from django.db import models

from .common_info import CommonInfo


class Psychologist(CommonInfo):
    psychologist = models.OneToOneField(
        User,
        verbose_name="Psicólogo(a)",
        on_delete=models.CASCADE,
    )
    crp_register = models.CharField(
        "Registro CRP",
        max_length=20,
    )
    short_description = models.CharField(
        "Descrição curta",
        max_length=100,
        null=True,
        blank=True,
    )
    professional_address = models.CharField(
        "Endereço Profissional",
        max_length=200,
    )
    city = models.CharField(
        "Cidade",
        max_length=200,
        default="Passo Fundo-RS",
    )
    secondary_address = models.CharField(
        "Endereço secundário",
        max_length=200,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        "Telefone",
        max_length=15,
        null=True,
        blank=True,
    )
    cpf = models.CharField(
        "CPF",
        null=True,
        blank=True,
        max_length=20,
    )
    instagram_link = models.CharField(
        "Link Instagram Profissional",
        null=True,
        blank=True,
        max_length=100,
    )
    twitter_link = models.CharField(
        "Link Twitter Profissional",
        null=True,
        blank=True,
        max_length=100,
    )
    linkedin_link = models.CharField(
        "Link LinkedIn Profissional",
        null=True,
        blank=True,
        max_length=100,
    )
    whatsapp_number = models.CharField(
        "WhatsApp Profissional",
        max_length=20,
        null=True,
        blank=True,
    )
    bio = models.TextField(
        "Biografia/Descrição",
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        "Imagem de Perfil",
        upload_to="media",
        null=True,
        blank=True,
    )
    schedule_description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Psicólogo"
        verbose_name_plural = "Psicólogos"

    def __str__(self):
        return self.psychologist.first_name
