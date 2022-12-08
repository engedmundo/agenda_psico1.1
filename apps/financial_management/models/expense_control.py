from apps.core.models import CommonInfo, Psychologist
from apps.financial_management.models import ExpenseCategory
from django.db import models


class ExpenseControl(CommonInfo):
    psychologist = models.ForeignKey(
        Psychologist,
        verbose_name="Profissional responsável",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        ExpenseCategory,
        verbose_name="Categoria da despesa",
        on_delete=models.CASCADE,
    )
    expense_value = models.DecimalField(
        "Valor da despesa", max_digits=8, decimal_places=2
    )
    completion_date = models.DateField("Data de pagamento")
    description = models.TextField(
        "Descrição da despesa",
        null=True,
        blank=True,
    )
    cpf_cnpj = models.CharField(
        verbose_name="CPF/CNPJ despesa",
        max_length=20,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Controle de despesa"
        verbose_name_plural = "Controle de despesas"

    def __str__(self):
        return self.description
