# Generated by Django 3.0.5 on 2021-04-08 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventassap',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 8, 9, 44, 54, 137890)),
        ),
    ]