# Generated by Django 3.0.5 on 2020-04-19 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200419_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 19, 16, 20, 2, 154182)),
        ),
        migrations.AlterField(
            model_name='grouprole',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 19, 16, 20, 2, 156176)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 19, 16, 20, 2, 153185)),
        ),
    ]
