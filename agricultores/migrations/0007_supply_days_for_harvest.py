# Generated by Django 3.1.5 on 2021-04-03 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agricultores', '0006_auto_20210303_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='days_for_harvest',
            field=models.IntegerField(default=0),
        ),
    ]
