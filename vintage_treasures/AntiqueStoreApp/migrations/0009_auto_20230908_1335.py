# Generated by Django 3.0 on 2023-09-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AntiqueStoreApp', '0008_auto_20230908_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='end_time',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='auction',
            name='start_time',
            field=models.CharField(max_length=200),
        ),
    ]
