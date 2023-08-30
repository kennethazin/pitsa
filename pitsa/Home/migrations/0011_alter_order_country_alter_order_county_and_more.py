# Generated by Django 4.1.6 on 2023-02-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_order_country_order_county_order_door_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(default='Ireland', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='door_no',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='eircode',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='street',
            field=models.CharField(default='', max_length=50),
        ),
    ]
