# Generated by Django 3.2.15 on 2022-10-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leilao", "0004_auto_20221009_1736"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bids",
            name="product",
            field=models.IntegerField(),
        ),
    ]
