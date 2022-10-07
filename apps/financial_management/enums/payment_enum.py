from django.db import models


class PaymentChoices(models.TextChoices):
    PIX = "Pix"
    MONEY = "Dinheiro"
    TRASNFERENCY = "Transferência"
    CHECK = "Cheque"
