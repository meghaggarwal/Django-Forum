# Generated by Django 3.0.7 on 2020-06-23 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20200623_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]