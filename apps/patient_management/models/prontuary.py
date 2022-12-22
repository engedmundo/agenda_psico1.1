from apps.core.models import CommonInfo, ServiceModalitiy
from apps.patient_management.models import Patient
from django.db import models


class Prontuary(CommonInfo):
    patient = models.ForeignKey(
        Patient,
        verbose_name="Paciente",
        on_delete=models.CASCADE,
    )
    prontuary_number = models.CharField(
        verbose_name="Número do prontuário",
        max_length=10,
        default="1",
    )
    open_date = models.DateField(
        verbose_name="Data de abertura",
    )
    close_date = models.DateField(
        verbose_name="Data de fechamento",
        null=True,
        blank=True,
    )
    demand_description = models.TextField(
        verbose_name="Avaliação da demanda",
    )
    type_of_service = models.ForeignKey(
        ServiceModalitiy,
        verbose_name="Tipo de atendimento",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Prontuário"
        verbose_name_plural = "Prontuários"

    def __str__(self):
        return f"{str(self.patient)} | Prontuário {str(self.prontuary_number)}"
