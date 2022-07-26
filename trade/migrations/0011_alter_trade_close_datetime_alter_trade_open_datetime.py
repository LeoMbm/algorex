# Generated by Django 4.0.6 on 2022-07-26 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0010_alter_trade_open_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='close_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='open_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 26, 18, 45, 29, 622335)),
        ),
    ]