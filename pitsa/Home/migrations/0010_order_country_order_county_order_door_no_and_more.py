# Generated by Django 4.1.6 on 2023-02-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_alter_order_delivery_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='county',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='door_no',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='eircode',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(default=''),
        ),
    ]
