# Generated by Django 3.1.3 on 2020-11-07 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_auto_20201107_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='height',
        ),
        migrations.AddField(
            model_name='place',
            name='iron_grate',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
