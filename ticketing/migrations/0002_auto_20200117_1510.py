# Generated by Django 2.2.7 on 2020-01-17 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ticketing.Localtion'),
        ),
    ]
