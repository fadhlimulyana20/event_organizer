# Generated by Django 2.2.7 on 2020-02-01 02:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0014_auto_20200126_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='due_registeration',
            field=models.DateField(default=datetime.datetime(2020, 2, 2, 9, 20, 7, 794219)),
        ),
    ]