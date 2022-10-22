# Generated by Django 4.1.2 on 2022-10-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_psychologist_bio_psychologist_instagram_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="psychologist",
            name="short_description",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Descrição curta"
            ),
        ),
    ]