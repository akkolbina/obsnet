# Generated by Django 3.1.5 on 2021-04-14 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obsnet', '0004_auto_20210412_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='id_adt',
        ),
        migrations.RemoveField(
            model_name='econfields',
            name='id_adt',
        ),
        migrations.RemoveField(
            model_name='fed_o',
            name='id_adt',
        ),
        migrations.RemoveField(
            model_name='subrf',
            name='id_adt',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='id_adt',
        ),
        migrations.RemoveField(
            model_name='weatherstation',
            name='id_country',
        ),
        migrations.AddField(
            model_name='adt',
            name='id_country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='obsnet.country'),
        ),
    ]
