# Generated by Django 4.2.9 on 2024-01-23 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdvertCompany",
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
                    "name",
                    models.CharField(max_length=200, verbose_name="название компании"),
                ),
                (
                    "promotion_channel",
                    models.CharField(max_length=500, verbose_name="канал продвижения"),
                ),
                (
                    "budget",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        verbose_name="бюджет на рекламу",
                    ),
                ),
                (
                    "service_advert",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="services.servicesmodel",
                    ),
                ),
            ],
        ),
    ]
