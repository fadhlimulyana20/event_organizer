# Generated by Django 2.2.7 on 2020-01-17 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0006_auto_20200117_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_participant',
            name='role',
            field=models.CharField(choices=[('1', 'Peserta'), ('2', 'Narasumber')], default='1', max_length=1),
        ),
    ]