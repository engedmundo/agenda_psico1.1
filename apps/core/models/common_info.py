from django.db import models


class CommonInfo(models.Model):
    created_at = models.DateField("Data de criação", auto_now_add=True)
    updated_at = models.DateField("Data de atualização", auto_now=True)
    is_active = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True
