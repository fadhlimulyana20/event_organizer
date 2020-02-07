# Generated by Django 2.2.7 on 2020-02-05 23:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0027_auto_20200206_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='due_registration',
            field=models.DateField(default=datetime.datetime(2020, 2, 3, 6, 35, 14, 572056)),
        ),
        migrations.AlterField(
            model_name='eventpayment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 23, 35, 14, 576061, tzinfo=utc)),
        ),
    ]