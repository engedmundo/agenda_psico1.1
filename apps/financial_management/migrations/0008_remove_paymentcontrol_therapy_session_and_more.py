# Generated by Django 4.1.2 on 2022-12-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "financial_management",
            "0007_rename_data_pay_paymentcontrol_date_of_pay_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="paymentcontrol",
            name="therapy_session",
        ),
        migrations.AlterField(
            model_name="paymentcontrol",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("Pix", "Pix"),
                    ("Dinheiro", "Dinheiro"),
                    ("Transferência", "Tranferencia"),
                    ("Cheque", "Cheque"),
                    ("Cartão de Crédito", "Cartao De Credito"),
                ],
                max_length=50,
                verbose_name="Forma de pagamento",
            ),
        ),
    ]
