# Generated by Django 2.2.7 on 2020-02-01 04:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0016_remove_event_due_registeration'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='due_registeration',
            field=models.DateField(default=datetime.datetime(2020, 1, 29, 11, 3, 16, 221052)),
        ),
    ]
