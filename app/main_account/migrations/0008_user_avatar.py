# Generated by Django 3.2.5 on 2021-07-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_account', '0007_alter_logologin_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]