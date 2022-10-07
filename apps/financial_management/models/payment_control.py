from apps.core.models import CommonInfo
from apps.financial_management.enums.payment_enum import PaymentChoices
from apps.patient_management.models import Patient
from django.db import models


class PaymentControl(CommonInfo):
    pacient = models.ForeignKey(
        Patient, verbose_name="Paciente", on_delete=models.CASCADE
    )
    value_pay = models.DecimalField("Valor pago", max_digits=8, decimal_places=2)
    data_pay = models.DateField("Data de pagamento")
    description = models.CharField(
        "Descrição do pagamento", null=True, blank=True, max_length=100
    )
    way_pay = models.CharField(
        "Forma de pagamento", choices=PaymentChoices.choices, max_length=50
    )
    # associar sessions aos pagamentos

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __str__(self):
        return self.description
