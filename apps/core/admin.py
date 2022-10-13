from django.contrib import admin

from .models import Psychologist


@admin.register(Psychologist)
class PsycologistAdmin(admin.ModelAdmin):
    list_display = ["psychologist", "crp_register", "phone_number"]
    search_fields = [
        "psychologist",
        "cpf",
    ]
