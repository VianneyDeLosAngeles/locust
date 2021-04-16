# Generated by Django 3.0.5 on 2021-04-08 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0004_auto_20210408_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventassap',
            name='canal',
        ),
        migrations.AddField(
            model_name='ventassap',
            name='texto',
            field=models.CharField(help_text='Texto', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ventassap',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 8, 16, 36, 26, 401651)),
        ),
    ]
