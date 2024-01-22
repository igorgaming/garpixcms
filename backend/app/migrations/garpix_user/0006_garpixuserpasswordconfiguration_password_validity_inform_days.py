# Generated by Django 3.2 on 2023-11-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_user', '0005_garpixuserpasswordconfiguration_passwordhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='garpixuserpasswordconfiguration',
            name='password_validity_inform_days',
            field=models.IntegerField(default=-1, help_text='-1 если отправка уведомлений не требуется', verbose_name='За сколько дней начинать отправлять уведомление об истечении срока пароля'),
        ),
    ]