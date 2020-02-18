# Generated by Django 2.2.7 on 2020-02-18 14:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0047_auto_20200218_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='due_registration',
            field=models.DateField(default=datetime.datetime(2020, 2, 15, 21, 53, 15, 110013)),
        ),
        migrations.AlterField(
            model_name='eventpayment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 14, 53, 15, 110013, tzinfo=utc)),
        ),
    ]
