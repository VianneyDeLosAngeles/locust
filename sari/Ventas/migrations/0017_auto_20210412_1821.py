# Generated by Django 3.0.5 on 2021-04-12 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0016_auto_20210412_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuento',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 12, 18, 21, 23, 611151)),
        ),
        migrations.AlterField(
            model_name='uuid_asw',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 12, 18, 21, 23, 623516)),
        ),
        migrations.AlterField(
            model_name='ventasasw',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 12, 18, 21, 23, 657560)),
        ),
        migrations.AlterField(
            model_name='ventassap',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 12, 18, 21, 23, 661841)),
        ),
    ]
