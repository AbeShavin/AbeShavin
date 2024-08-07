# Generated by Django 5.0.6 on 2024-07-16 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_listing", "0005_alter_car_make_alter_car_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="latitude",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="car",
            name="longitude",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="car",
            name="zipcode",
            field=models.CharField(default="33021", max_length=10),
        ),
    ]
