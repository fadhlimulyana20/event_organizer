# Generated by Django 2.2.7 on 2020-01-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0001_initial'),
        ('ticketing', '0012_dataevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='data',
            field=models.ManyToManyField(related_name='data_event', through='ticketing.DataEvent', to='filemanager.Data'),
        ),
    ]