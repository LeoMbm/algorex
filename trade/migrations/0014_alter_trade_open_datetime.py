# Generated by Django 4.0.6 on 2022-07-27 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0013_alter_trade_close_datetime_alter_trade_open_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='open_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 27, 19, 46, 40, 479280)),
        ),
    ]