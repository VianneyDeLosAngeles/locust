# Generated by Django 3.0.5 on 2021-04-12 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0009_auto_20210412_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuento',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 12, 11, 18, 59, 838414)),
        ),
        migrations.AlterField(
            model_name='uuid_asw',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 12, 11, 18, 59, 843444)),
        ),
        migrations.AlterField(
            model_name='ventasasw',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 12, 11, 18, 59, 859233)),
        ),
        migrations.AlterField(
            model_name='ventasasw',
            name='periodoContable',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='ventassap',
            name='fechaInsercion',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 12, 11, 18, 59, 859233)),
        ),
    ]