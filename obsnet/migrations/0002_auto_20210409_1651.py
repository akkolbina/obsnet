# Generated by Django 3.1.5 on 2021-04-09 13:51

import django.contrib.gis.db.models.fields
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('obsnet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='adt',
            managers=[
                ('objects_adt', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='adt',
            name='adt_border',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]