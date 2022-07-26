# Generated by Django 4.0.6 on 2022-07-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='open',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
