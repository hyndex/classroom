# Generated by Django 3.0.5 on 2020-04-19 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200417_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 19, 15, 51, 54, 47001)),
        ),
        migrations.AlterField(
            model_name='grouprole',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 19, 15, 51, 54, 48994)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 19, 15, 51, 54, 46003)),
        ),
    ]
