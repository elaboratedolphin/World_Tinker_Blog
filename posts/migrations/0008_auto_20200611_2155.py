# Generated by Django 3.0.3 on 2020-06-12 04:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200607_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 12, 4, 55, 19, 155834, tzinfo=utc)),
        ),
    ]