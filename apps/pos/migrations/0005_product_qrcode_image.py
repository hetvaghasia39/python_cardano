# Generated by Django 4.1 on 2022-08-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pos", "0004_remove_product_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="qrcode_image",
            field=models.ImageField(default="nothing", upload_to=""),
            preserve_default=False,
        ),
    ]
