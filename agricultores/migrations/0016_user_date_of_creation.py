# Generated by Django 3.1.5 on 2021-05-17 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agricultores', '0015_auto_20210419_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
