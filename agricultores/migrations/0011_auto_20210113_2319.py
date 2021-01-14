# Generated by Django 3.1.5 on 2021-01-13 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agricultores', '0010_auto_20210113_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='supplies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agricultores.supply'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='publish',
            name='supplies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agricultores.supply'),
        ),
        migrations.AlterField(
            model_name='publish',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agricultores.district'),
        ),
    ]
