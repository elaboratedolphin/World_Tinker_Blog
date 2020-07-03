# Generated by Django 3.0.3 on 2020-06-18 06:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200617_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='rating',
            new_name='views',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 6, 15, 35, 348967, tzinfo=utc)),
        ),
    ]