# Generated by Django 4.1 on 2022-08-26 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pos", "0002_product_delete_products"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="product_owner",
        ),
    ]