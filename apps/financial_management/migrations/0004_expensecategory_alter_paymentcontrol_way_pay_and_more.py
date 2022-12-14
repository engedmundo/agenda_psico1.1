# Generated by Django 4.1.2 on 2022-10-24 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_servicemodalitiy"),
        ("financial_management", "0003_alter_paymentcontrol_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExpenseCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now=True, verbose_name="Data de criação"),
                ),
                (
                    "updated_at",
                    models.DateField(auto_now=True, verbose_name="Data de atualização"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Ativo")),
                (
                    "name",
                    models.CharField(max_length=50, verbose_name="Nome da categoria"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Descrição da modalidade"
                    ),
                ),
                (
                    "psychologist",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.psychologist",
                        verbose_name="Profissional responsável",
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoria de despesa",
                "verbose_name_plural": "Categorias de despesa",
            },
        ),
        migrations.AlterField(
            model_name="paymentcontrol",
            name="way_pay",
            field=models.CharField(
                choices=[
                    ("Pix", "Pix"),
                    ("Dinheiro", "Dinheiro"),
                    ("Transferência", "Tranferencia"),
                    ("Cheque", "Cheque"),
                ],
                max_length=50,
                verbose_name="Forma de pagamento",
            ),
        ),
        migrations.CreateModel(
            name="ExpenseControl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now=True, verbose_name="Data de criação"),
                ),
                (
                    "updated_at",
                    models.DateField(auto_now=True, verbose_name="Data de atualização"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Ativo")),
                (
                    "expense_value",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Valor da despesa"
                    ),
                ),
                ("completion_date", models.DateField(verbose_name="Data de pagamento")),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Descrição da despesa"
                    ),
                ),
                (
                    "cpf_cnpj",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="CPF/CNPJ despesa",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="financial_management.expensecategory",
                        verbose_name="Categoria da despesa",
                    ),
                ),
                (
                    "psychologist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.psychologist",
                        verbose_name="Profissional responsável",
                    ),
                ),
            ],
            options={
                "verbose_name": "Controle de despesa",
                "verbose_name_plural": "Controle de despesas",
            },
        ),
    ]
