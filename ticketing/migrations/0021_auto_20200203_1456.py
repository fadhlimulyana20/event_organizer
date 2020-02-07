# Generated by Django 2.2.7 on 2020-02-03 07:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0020_auto_20200202_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpayment',
            name='image_receipt',
            field=models.ImageField(blank=True, null=True, upload_to='images/transfer_receipt/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='due_registration',
            field=models.DateField(default=datetime.datetime(2020, 1, 31, 14, 56, 58, 449231)),
        ),
        migrations.AlterField(
            model_name='eventpayment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 7, 56, 58, 449231, tzinfo=utc)),
        ),
    ]
