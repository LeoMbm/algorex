# Generated by Django 4.0.6 on 2022-07-29 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0014_alter_trade_open_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='open_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 29, 11, 44, 58, 647123)),
        ),
    ]