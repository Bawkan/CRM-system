# Generated by Django 4.2.9 on 2024-01-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContractModel",
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
                ("name", models.CharField(max_length=100, verbose_name="название")),
                (
                    "service",
                    models.TextField(
                        max_length=2500, verbose_name="предоставление услуги"
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        upload_to="file", verbose_name="файл с документом"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="дата:"),
                ),
                ("start_date", models.DateTimeField(verbose_name="с:")),
                ("end_date", models.DateTimeField(verbose_name="до:")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="сумма"
                    ),
                ),
            ],
        ),
    ]