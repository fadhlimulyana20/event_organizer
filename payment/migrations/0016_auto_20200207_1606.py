# Generated by Django 2.2.7 on 2020-02-07 09:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0015_auto_20200206_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='image_receipt',
            field=models.ImageField(blank=True, null=True, upload_to='images/transfer_receipt/'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='pay_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 9, 9, 6, 8, 771663, tzinfo=utc)),
        ),
    ]
