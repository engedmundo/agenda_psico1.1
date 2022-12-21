from apps.financial_management.models import PaymentControl
from django import forms

class PaymentControlRegisterForm(forms.ModelForm):
    class Meta:
        model = PaymentControl
        fields = [
            "prontuary",
            "value_paid",
            "date_of_pay",
            "description",
            "payment_method",
            "therapy_session",
            "checking_copy",
        ]

        labels = {
            "prontuary": "Prontuário:",
            "value_paid": "Valor pago (R$):",
            "date_of_pay": "Data do pagamento:",
            "description": "Descrição do pagamento:",
            "payment_method": "Método de pagamento",
            "therapy_session": "Sessões:",
            "checking_copy": "Comprovante de pagamento:",
        }
