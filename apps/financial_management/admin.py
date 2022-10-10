from django.contrib import admin

from .models import PaymentControl, PaymentPlain


@admin.register(PaymentPlain)
class PaymentPlainAdmin(admin.ModelAdmin):
    list_display = ["name_plain", "plain_value"]
    list_filter = [
        "name_plain",
        "plain_value",
    ]
    search_fields = [
        "name_plain",
    ]


@admin.register(PaymentControl)
class PaymentControlAdmin(admin.ModelAdmin):
    list_display = ["pacient", "data_pay", "value_pay", "way_pay"]
    list_filter = ["pacient", "data_pay", "value_pay", "way_pay"]
    search_fields = ["pacient"]
