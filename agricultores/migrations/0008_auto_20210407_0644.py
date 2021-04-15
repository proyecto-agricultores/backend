# Generated by Django 3.1.5 on 2021-04-07 06:44

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agricultores', '0007_supply_days_for_harvest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='reach',
            new_name='remaining_credits',
        ),
        migrations.RemoveField(
            model_name='addressedto',
            name='district',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='harvest_date',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='sowing_date',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='supply',
        ),
        migrations.AddField(
            model_name='addressedto',
            name='supply',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agricultores.supply'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='beginning_harvest_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='beginning_sowing_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='agricultores.department'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='agricultores.district'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='ending_harvest_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='ending_sowing_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='for_orders',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='for_publications',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='picture_URLs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='agricultores.region'),
        ),
        migrations.AlterField(
            model_name='addressedto',
            name='advertisement',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agricultores.advertisement'),
        ),
    ]
