# Generated by Django 3.2 on 2021-04-15 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0003_alacarte_buffet_meal_mealorder_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buffet',
            name='meal_time',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterModelTable(
            name='alacarte',
            table='AlaCarte',
        ),
        migrations.AlterModelTable(
            name='buffet',
            table='Buffet',
        ),
        migrations.AlterModelTable(
            name='order',
            table='Order',
        ),
    ]
