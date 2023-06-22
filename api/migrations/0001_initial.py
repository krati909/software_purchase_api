# Generated by Django 4.2.2 on 2023-06-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Purchase",
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
                ("item", models.CharField(max_length=255)),
                ("department", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("transaction_date", models.DateTimeField()),
            ],
        ),
    ]