# Generated by Django 2.2.7 on 2020-02-13 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20200213_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Address'),
        ),
    ]