# Generated by Django 3.2.8 on 2021-10-31 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('population_tracker', '0003_auto_20211030_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor_data',
            name='id',
        ),
        migrations.AlterField(
            model_name='sensor_data',
            name='person_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]