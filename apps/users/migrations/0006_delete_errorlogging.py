# Generated by Django 4.1 on 2022-08-09 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_token_device_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ErrorLogging",
        ),
    ]