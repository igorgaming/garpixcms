# Generated by Django 3.2 on 2022-08-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_notify', '0011_auto_20220822_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemnotify',
            name='data_json',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='Данные JSON'),
        ),
    ]