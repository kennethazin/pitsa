# Generated by Django 4.1.6 on 2023-02-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_rename_id_order_order_id_order_delivery_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(default='', max_length=50),
        ),
    ]