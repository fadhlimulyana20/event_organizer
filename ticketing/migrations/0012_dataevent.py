# Generated by Django 2.2.7 on 2020-01-26 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0001_initial'),
        ('ticketing', '0011_delete_event_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filemanager.Data')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketing.Event')),
            ],
        ),
    ]
