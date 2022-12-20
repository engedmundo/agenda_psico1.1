from apps.core.models import CommonInfo, Psychologist
from django.db import models


class ServiceModalitiy(CommonInfo):
    psychologist = models.ForeignKey(
        Psychologist,
        verbose_name="Profissional",
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        "Nome da modalidade",
        max_length=50,
    )
    description = models.TextField(
        "Descrição da modalidade",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Modalidade de atendimento"
        verbose_name_plural = "Modalidades de atendimento"

    def __str__(self):
        return self.name
