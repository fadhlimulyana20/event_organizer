# Generated by Django 2.2.7 on 2020-02-13 14:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0040_auto_20200213_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='due_registration',
            field=models.DateField(default=datetime.datetime(2020, 2, 10, 21, 38, 55, 298428)),
        ),
        migrations.AlterField(
            model_name='eventpayment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 15, 14, 38, 55, 298428, tzinfo=utc)),
        ),
    ]