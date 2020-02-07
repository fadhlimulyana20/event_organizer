# Generated by Django 2.2.7 on 2020-02-06 00:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_auto_20200206_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 8, 0, 34, 20, 300170, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed Account', max_length=100)),
                ('invoice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payment.Invoice')),
            ],
        ),
    ]
