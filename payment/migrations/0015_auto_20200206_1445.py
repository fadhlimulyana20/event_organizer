# Generated by Django 2.2.7 on 2020-02-06 07:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0014_auto_20200206_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 8, 7, 45, 51, 298243, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='release_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]