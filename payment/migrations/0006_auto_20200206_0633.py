# Generated by Django 2.2.7 on 2020-02-05 23:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20200206_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 23, 33, 39, 746631, tzinfo=utc)),
        ),
    ]
