# Generated by Django 4.2.4 on 2023-08-15 05:57

import cities_income.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cities_income", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="actualprofit",
            options={
                "verbose_name": "Прибыль(факт.)",
                "verbose_name_plural": "Прибыль(факт.)",
            },
        ),
        migrations.AlterModelOptions(
            name="cities",
            options={"verbose_name": "Город", "verbose_name_plural": "Города"},
        ),
        migrations.AlterModelOptions(
            name="planprofit",
            options={
                "verbose_name": "Прибыль(план)",
                "verbose_name_plural": "Прибыль(план)",
            },
        ),
        migrations.AlterField(
            model_name="actualprofit",
            name="year",
            field=models.IntegerField(
                validators=[cities_income.validators.validate_year], verbose_name="Год"
            ),
        ),
        migrations.AlterField(
            model_name="planprofit",
            name="year",
            field=models.IntegerField(
                validators=[cities_income.validators.validate_year], verbose_name="Год"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="actualprofit",
            unique_together={("year", "city")},
        ),
    ]
