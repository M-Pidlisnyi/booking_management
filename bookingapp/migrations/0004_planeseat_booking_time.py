# Generated by Django 5.0.3 on 2024-09-20 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0003_alter_passenger_options_alter_planeseat_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='planeseat',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 20, 19, 23, 52, 586846)),
        ),
    ]
