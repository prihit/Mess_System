# Generated by Django 3.2 on 2021-04-15 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0005_alter_alacarte_meal_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealorder',
            name='meal_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mess.meal'),
        ),
        migrations.AlterField(
            model_name='mealorder',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mess.order'),
        ),
    ]