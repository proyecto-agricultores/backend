# Generated by Django 3.1.5 on 2021-01-25 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agricultores', '0003_auto_20210121_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publish',
            name='supplies',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplies_set', to='agricultores.supply'),
        ),
    ]
