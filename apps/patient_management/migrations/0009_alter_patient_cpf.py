# Generated by Django 4.1.2 on 2022-12-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient_management", "0008_prontuary_type_of_service"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="cpf",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="CPF"
            ),
        ),
    ]
