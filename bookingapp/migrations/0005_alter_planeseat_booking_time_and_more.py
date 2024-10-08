# Generated by Django 5.0.3 on 2024-09-20 17:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0004_planeseat_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planeseat',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 20, 20, 4, 42, 75161)),
        ),
        migrations.AlterField(
            model_name='planeseat',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingapp.passenger'),
        ),
    ]
