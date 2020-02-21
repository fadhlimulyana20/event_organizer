# Generated by Django 2.2.7 on 2020-02-15 06:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0044_auto_20200215_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='due_registration',
            field=models.DateField(default=datetime.datetime(2020, 2, 12, 13, 5, 31, 855677)),
        ),
        migrations.AlterField(
            model_name='eventpayment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 6, 5, 31, 859666, tzinfo=utc)),
        ),
    ]