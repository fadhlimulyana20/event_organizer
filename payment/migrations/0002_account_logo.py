# Generated by Django 2.2.7 on 2020-02-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/payment/account/'),
        ),
    ]