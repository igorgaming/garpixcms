# Generated by Django 3.2 on 2023-11-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20231107_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='keycloak_auth_only',
            field=models.BooleanField(default=False, verbose_name='Авторизация только через keycloak'),
        ),
    ]
