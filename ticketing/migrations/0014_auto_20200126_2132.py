# Generated by Django 2.2.7 on 2020-01-26 14:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticketing', '0013_event_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event_participant',
            new_name='EventParticipant',
        ),
    ]
