# Generated by Django 3.1.5 on 2021-04-09 13:52

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obsnet', '0002_auto_20210409_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherstation',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT EMPTY', srid=4326),
        ),
    ]
