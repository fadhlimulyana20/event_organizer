# Generated by Django 2.2.7 on 2020-02-05 23:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20200206_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(default='Unnamed Account', max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='provider',
            field=models.CharField(default='Unnamed Provider', max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 23, 31, 38, 82970, tzinfo=utc)),
        ),
    ]
