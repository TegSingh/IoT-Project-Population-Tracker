# Generated by Django 3.1.3 on 2021-10-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_number', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
