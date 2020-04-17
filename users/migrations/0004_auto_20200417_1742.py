# Generated by Django 3.0.5 on 2020-04-17 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200415_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 17, 42, 24, 319887)),
        ),
        migrations.AlterField(
            model_name='grouprole',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 17, 42, 24, 322884)),
        ),
        migrations.AlterField(
            model_name='grouprole',
            name='role',
            field=models.TextField(default='student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 17, 17, 42, 24, 318892)),
        ),
    ]
