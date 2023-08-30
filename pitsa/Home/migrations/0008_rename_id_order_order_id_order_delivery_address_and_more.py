# Generated by Django 4.1.6 on 2023-02-27 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_order_payment_pizzasauce_price_delete_pizza_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='id',
            new_name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='additional_toppings',
            field=models.ManyToManyField(blank=True, related_name='additional_topping_orders', to='Home.pizzatopping'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='selected_topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_topping_orders', to='Home.pizzatopping'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
