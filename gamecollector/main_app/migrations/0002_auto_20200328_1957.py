# Generated by Django 3.0.4 on 2020-03-28 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='year',
        ),
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Released Year'),
            preserve_default=False,
        ),
    ]
