# Generated by Django 2.2.7 on 2020-02-18 07:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0025_auto_20200218_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 7, 47, 0, 584764, tzinfo=utc)),
        ),
    ]