# Generated by Django 2.2.7 on 2020-02-15 05:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0022_auto_20200215_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 17, 5, 4, 35, 87916, tzinfo=utc)),
        ),
    ]
