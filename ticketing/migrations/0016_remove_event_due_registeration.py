# Generated by Django 2.2.7 on 2020-02-01 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0015_event_due_registeration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='due_registeration',
        ),
    ]
