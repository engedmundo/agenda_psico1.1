from django.db import models


class PaymentChoices(models.TextChoices):
    PIX = "Pix"
    DINHEIRO = "Dinheiro"
    TRANFERENCIA = "Transferência"
    CHEQUE = "Cheque"
    CARTAO_DE_CREDITO = "Cartão de Crédito"
