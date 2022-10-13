from apps.core.models import CommonInfo
from apps.patient_management.models import Patient
from django.db import models


class Prontuary(CommonInfo):
    patient = models.OneToOneField(
        Patient, verbose_name="Paciente", on_delete=models.CASCADE
    )
    open_date = models.DateField("Data de abertura")
    close_date = models.DateField("Data de fechamento", null=True, blank=True)
    demand_description = models.TextField("Avaliação da demanda")

    class Meta:
        verbose_name = "Prontuário"
        verbose_name_plural = "Prontuários"

    def __str__(self):
        return str(self.patient)
