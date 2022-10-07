from apps.core.models import CommonInfo, Psychologist
from django.db import models


class PaymentPlain(CommonInfo):
    psycologist = models.ForeignKey(
        Psychologist,
        verbose_name="Profissional responsável",
        on_delete=models.SET_NULL,
        null=True,
    )
    name_plain = models.CharField(
        "Descrição", 
        max_length=30
    )
    plain_value = models.DecimalField(
        "Valor Plano (R$)",
        max_digits=8,
        decimal_places=2,
    )

    class Meta:
        verbose_name = "Plano de pagamento"
        verbose_name_plural = "Planos de pagamento"

    def __str__(self):
        return self.name_plain
