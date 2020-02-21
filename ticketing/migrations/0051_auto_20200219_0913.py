# Generated by Django 2.2.7 on 2020-02-19 02:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0050_auto_20200219_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date_of_release',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='due_registration',
            field=models.DateField(default=datetime.datetime(2020, 2, 16, 9, 13, 22, 888748)),
        ),
        migrations.AlterField(
            model_name='eventpayment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 21, 2, 13, 22, 890739, tzinfo=utc)),
        ),
    ]