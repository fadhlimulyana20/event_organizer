# Generated by Django 2.2.7 on 2020-02-06 07:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0033_auto_20200206_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='due_registration',
            field=models.DateField(default=datetime.datetime(2020, 2, 3, 14, 42, 43, 810296)),
        ),
        migrations.AlterField(
            model_name='eventpayment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 8, 7, 42, 43, 817660, tzinfo=utc)),
        ),
    ]
