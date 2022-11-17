from apps.core.models import CommonInfo
from apps.patient_management.models import Patient, Prontuary
from django.db import models


# Create your models here.
class TherapySession(CommonInfo):
    session_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient,
        verbose_name="Paciente",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    prontuary = models.ForeignKey(
        Prontuary,
        verbose_name="Prontuário",
        on_delete=models.CASCADE,
        default=False,
        null=True,
        blank=True,
    )
    session_number = models.CharField(
        "Número da sessão",
        max_length=10,
    )
    date_session = models.DateField(
        "Data da seção",
    )
    hour_session = models.TimeField(
        "Horário da sessão",
    )
    fault = models.BooleanField(
        "Paciente faltou?",
        default=False,
    )
    justify_fault = models.CharField(
        "Justificativa da falta",
        null=True,
        blank=True,
        max_length=500,
    )
    evolution = models.TextField(
        "Evolução do caso",
    )
    forwarding = models.TextField(
        "Encaminhamento",
        null=True,
        blank=True,
        max_length=5000,
    )
    payment = models.BooleanField(
        "Pagamento",
        default=False,
    )

    class Meta:
        verbose_name = "Sessão"
        verbose_name_plural = "Sessões"

    def __str__(self):
        return f"{self.patient} | Sessão {str(self.session_id)} | {self.date_session}"
