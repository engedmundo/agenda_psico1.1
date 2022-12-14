# Generated by Django 4.1.2 on 2022-12-19 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient_management", "0005_alter_therapysession_prontuary"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="discount_agreement",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Acordo de desconto"
            ),
        ),
        migrations.AddField(
            model_name="patient",
            name="session_value",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=8,
                null=True,
                verbose_name="Valor da sessão (R$)",
            ),
        ),
    ]
