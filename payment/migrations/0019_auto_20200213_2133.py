# Generated by Django 2.2.7 on 2020-02-13 14:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0018_auto_20200213_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 15, 14, 33, 7, 434388, tzinfo=utc)),
        ),
    ]
