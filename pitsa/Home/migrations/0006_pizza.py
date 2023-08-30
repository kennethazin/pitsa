# Generated by Django 4.1.6 on 2023-02-22 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_rename_cheeses_cheese'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheese', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.cheese')),
                ('crust', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.pizzacrust')),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.pizzasauce')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.pizzasize')),
                ('toppings', models.ManyToManyField(to='Home.pizzatopping')),
            ],
        ),
    ]
