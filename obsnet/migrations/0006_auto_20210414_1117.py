# Generated by Django 3.1.5 on 2021-04-14 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obsnet', '0005_auto_20210414_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subrf',
            name='id_country',
        ),
        migrations.RemoveField(
            model_name='subrf',
            name='id_fed_o',
        ),
    ]
