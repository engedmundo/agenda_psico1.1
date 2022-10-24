from apps.core.models import CommonInfo, Psychologist
from django.db import models


class ExpenseCategory(CommonInfo):
    psychologist = models.ForeignKey(
        Psychologist,
        verbose_name="Profissional responsável",
        on_delete=models.CASCADE,
        null=True,
    )
    name = models.CharField("Nome da categoria", max_length=50)
    description = models.TextField(
        "Descrição da modalidade",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Categoria de despesa"
        verbose_name_plural = "Categorias de despesa"

    def __str__(self):
        return self.name
