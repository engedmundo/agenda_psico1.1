from dataclasses import fields
from django import forms
from apps.financial_management.models import PaymentControl

class PaymentControlRegisterForm(forms.ModelForm):
    class Meta:
        model = PaymentControl
        fields = [
            'patient',
            'value_pay',
            'data_pay',
            'description',
            'way_pay',
        ]

        labels = {
            'patient': 'Nome do paciente',
            'value_pay': 'Valor pago (R$)',
            'data_pay': 'Data do pagamento',
            'description': 'Descrição do pagamento',
            'way_pay': 'Forma de pagamento',
        }

        placeholder = {
            'patient': 'Selecione o paciente',
            'value_pay': 'R$',
            'description': 'Pagamento referente a ...',
            'way_pay': 'Selecione a forma de pagamento',
        }