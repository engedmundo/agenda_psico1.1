# Generated by Django 4.1.2 on 2022-12-22 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_alter_psychologist_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="psychologist",
            name="city",
            field=models.CharField(
                default="Passo Fundo-RS", max_length=200, verbose_name="Cidade"
            ),
        ),
    ]
