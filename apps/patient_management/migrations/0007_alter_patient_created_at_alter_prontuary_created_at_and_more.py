# Generated by Django 4.1.2 on 2022-12-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient_management", "0006_patient_discount_agreement_patient_session_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="Data de criação"),
        ),
        migrations.AlterField(
            model_name="prontuary",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="Data de criação"),
        ),
        migrations.AlterField(
            model_name="therapysession",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="Data de criação"),
        ),
    ]