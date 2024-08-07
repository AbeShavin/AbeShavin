# Generated by Django 5.0.6 on 2024-07-15 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_listing", "0003_rename_seller_car_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarImage",
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
                ("image", models.ImageField(upload_to="car_images/")),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="additional_images",
                        to="car_listing.car",
                    ),
                ),
            ],
        ),
    ]
