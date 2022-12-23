from apps.core.models import CommonInfo
from apps.financial_management.enums.payment_enum import PaymentChoices
from apps.patient_management.models import Patient, TherapySession, Prontuary
from django.db import models


class PaymentControl(CommonInfo):
    prontuary = models.ForeignKey(
        Prontuary,
        verbose_name="Prontuário",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    value_paid = models.DecimalField(
        "Valor pago",
        max_digits=8,
        decimal_places=2,
    )
    date_of_pay = models.DateField(
        "Data de pagamento",
    )
    description = models.TextField(
        "Descrição do pagamento",
        null=True,
        blank=True,
    )
    payment_method = models.CharField(
        "Forma de pagamento",
        choices=PaymentChoices.choices,
        max_length=50,
    )
    checking_copy = models.ImageField(
        "Comprovante de pagamento",
        upload_to="media",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __str__(self):
        return self.description
